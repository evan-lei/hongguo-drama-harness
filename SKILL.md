---
name: hongguo-drama-harness
description: Manage the 红果短剧剧本 Harness 体系 (hongguo-drama-harness repo). Use when the user wants to create short drama scripts for 红果短剧, enrich story ideas, manage prompts/skills, or work on drama projects in this harness.
---

# 红果短剧 Harness 管理指南

## 仓库信息

| 项目 | 值 |
|------|-----|
| GitHub 仓库 | `https://github.com/evan-lei/hongguo-drama-harness` |
| 本地工作目录 | `/Users/user/Documents/hongguo-drama-harness` |
| GitHub 用户名 | `evan-lei` |

Token 见 `~/.cursor/skills/evan-lei-github-pages/SKILL.md`。

## 目录结构

```
hongguo-drama-harness/
├── SKILL.md              # 本文件
├── README.md
├── ROADMAP.md            # Skill 路线图
├── skills/               # Cursor Skills 源文件
│   ├── hongguo-platform/
│   └── drama-prompt-enrich/
├── prompts/              # Prompt 片段库
└── projects/             # 具体剧本项目
    └── <剧名>/
        ├── brief.md      # 故事初稿
        ├── outline.md    # 大纲
        └── episodes/     # 分集稿
```

## 推送到 GitHub

```bash
cd /Users/user/Documents/hongguo-drama-harness
git remote set-url origin https://evan-lei:<TOKEN>@github.com/evan-lei/hongguo-drama-harness.git
git add .
git commit -m "描述改动"
git push origin main
git remote set-url origin https://github.com/evan-lei/hongguo-drama-harness.git
```

## 创作工作流

用户有新想法时，按顺序加载 Skill：

1. **`drama-prompt-enrich`** — 碎片输入 → 故事初稿，保存到 `projects/<剧名>/brief.md`
2. **`hongguo-platform`** — 创作全程遵守平台规范与避坑
3. （后续）`drama-outline` → `drama-episode` → `drama-qc`

## 新建剧本项目

```bash
mkdir -p /Users/user/Documents/hongguo-drama-harness/projects/<剧名>/episodes
```

## Skill 同步到 Cursor

修改 `skills/` 后，若已建立 symlink 则自动生效；否则执行 README 中的 `ln -sf` 命令。
