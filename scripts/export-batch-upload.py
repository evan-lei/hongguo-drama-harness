#!/usr/bin/env python3
"""导出红果创服「剧本批量上传」格式单文件。"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

CN_DIGITS = "零一二三四五六七八九"


def episode_to_chinese_title(n: int) -> str:
    if n == 0:
        return "第零集"
    if n < 0 or n > 99:
        raise ValueError(f"集数超出支持范围: {n}")
    if n < 10:
        return f"第{CN_DIGITS[n]}集"
    if n == 10:
        return "第十集"
    if n < 20:
        return f"第十{CN_DIGITS[n % 10]}集"
    tens, ones = divmod(n, 10)
    tail = CN_DIGITS[ones] if ones else ""
    return f"第{CN_DIGITS[tens]}十{tail}集"


def extract_episode_body(text: str, ep_num: int) -> str:
    """去掉 Markdown 元数据，保留剧本正文；集标题改为中文数字。"""
    lines = text.splitlines()
    body: list[str] = []
    started = False
    for line in lines:
        if line.startswith("#") or line.startswith(">") or line.strip() == "---":
            continue
        if re.match(r"^第\d+集\s*$", line.strip()):
            started = True
            body.append(episode_to_chinese_title(ep_num))
            continue
        if started:
            body.append(line)
    return "\n".join(body).strip()


def build_episode_zero(brief_path: Path, outline_path: Path) -> str:
    brief = brief_path.read_text(encoding="utf-8") if brief_path.exists() else ""
    outline = outline_path.read_text(encoding="utf-8") if outline_path.exists() else ""

    parts = [episode_to_chinese_title(0), ""]

    # 人物小传：从 brief 核心人物段提取
    m = re.search(r"## 核心人物\n(.*?)\n## ", brief, re.S)
    if m:
        chars = m.group(1).strip()
        for block in re.split(r"\n### ", chars):
            block = block.strip()
            if not block:
                continue
            if block.startswith("### "):
                block = block[4:]
            name_line, _, rest = block.partition("\n")
            name = re.sub(r"（[^）]+）", "", name_line).strip()
            parts.append(f"人物小传：{name}")
            for line in rest.splitlines():
                line = line.strip()
                if line.startswith("- "):
                    parts.append(line[2:])
            parts.append("")

    # 剧本大纲：优先 outline 故事梗概
    m2 = re.search(r"### 故事梗概\n(.*?)\n### ", outline, re.S)
    if m2:
        parts.append("剧本大纲")
        outline_text = re.sub(r"\*\*", "", m2.group(1).strip())
        parts.append(outline_text)
    elif "## 一句话梗概" in brief:
        m3 = re.search(r"## 一句话梗概\n(.+)", brief)
        if m3:
            parts.append("剧本大纲")
            parts.append(m3.group(1).strip())

    return "\n".join(parts).strip()


def export_batch(project_dir: Path, include_episode_zero: bool = True) -> str:
    episodes_dir = project_dir / "episodes"
    if not episodes_dir.is_dir():
        raise FileNotFoundError(f"未找到 episodes 目录: {episodes_dir}")

    ep_files = sorted(
        episodes_dir.glob("ep*.md"),
        key=lambda p: int(re.search(r"ep(\d+)", p.name).group(1)),
    )
    if not ep_files:
        raise FileNotFoundError(f"未找到分集剧本: {episodes_dir}/ep*.md")

    sections: list[str] = []

    if include_episode_zero:
        ep0 = build_episode_zero(project_dir / "brief.md", project_dir / "outline.md")
        if ep0:
            sections.append(ep0)

    for ep_file in ep_files:
        n = int(re.search(r"ep(\d+)", ep_file.name).group(1))
        body = extract_episode_body(ep_file.read_text(encoding="utf-8"), n)
        if body:
            sections.append(body)

    return "\n\n".join(sections) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="导出红果剧本批量上传格式")
    parser.add_argument("project", type=Path, help="项目目录，如 projects/中子狂飙")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="输出文件路径（默认 <project>/upload-batch.txt）",
    )
    parser.add_argument(
        "--no-episode-zero",
        action="store_true",
        help="不包含第零集（人物小传+大纲）",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    out = args.output or (project / "upload-batch.txt")
    content = export_batch(project, include_episode_zero=not args.no_episode_zero)
    out.write_text(content, encoding="utf-8")
    print(f"已导出: {out}")
    print(f"集数: {content.count(chr(0x7b2c))} 个「第」标记（含第零集）")


if __name__ == "__main__":
    main()
