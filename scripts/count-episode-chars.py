#!/usr/bin/env python3
"""统计红果短剧分集剧本正文字数（汉字）。"""
import re
import sys
from pathlib import Path


def count_body_chinese(text: str) -> int:
    m = re.search(r"^第\d+集\s*$", text, re.MULTILINE)
    body = text[m.start() :] if m else text
    return len(re.findall(r"[\u4e00-\u9fff]", body))


def main() -> None:
    if len(sys.argv) < 2:
        print("用法: python3 scripts/count-episode-chars.py <episodes目录或单集.md>")
        sys.exit(1)

    path = Path(sys.argv[1])
    files = sorted(path.glob("ep*.md")) if path.is_dir() else [path]

    fail = []
    for f in files:
        n = count_body_chinese(f.read_text(encoding="utf-8"))
        ok = 300 <= n <= 2500
        tag = "OK" if ok else "FAIL"
        print(f"{f.name}: {n} 汉字 [{tag}]")
        if not ok:
            fail.append(f.name)

    if fail:
        print(f"\n未达标: {', '.join(fail)}（要求 300–2500 汉字）")
        sys.exit(1)
    print(f"\n全部 {len(files)} 集达标。")


if __name__ == "__main__":
    main()
