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
│   ├── hongguo-platform/     # 平台规范
│   ├── drama-prompt-enrich/  # 内容：故事初稿
│   ├── drama-outline/        # 内容：大纲
│   ├── drama-episode/        # 内容：分集剧本
│   ├── drama-qc/             # 内容：质检
│   ├── draft-build/          # 工具：初稿编排
│   ├── outline-build/        # 工具：大纲编排
│   ├── episode-build/        # 工具：剧本编排
│   ├── qc-build/             # 工具：质检编排
│   └── tools/README.md       # 两层架构说明
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

推荐用**工具 Skill**（用户 `@` 触发）：

| 步骤 | 工具 Skill | 产出 |
|------|------------|------|
| 1 | `@draft-build` | `projects/<剧名>/brief.md` |
| 2 | `@outline-build` | `projects/<剧名>/outline.md` |
| 3 | `@episode-build` | `projects/<剧名>/episodes/ep*.md` |
| 4 | `@qc-build` | `projects/<剧名>/qc-*.md` |

每个工具 Skill 内部自动加载对应内容 Skill + `hongguo-platform`。

## 新建剧本项目

```bash
mkdir -p /Users/user/Documents/hongguo-drama-harness/projects/<剧名>/episodes
```

## Skill 同步到 Cursor

修改 `skills/` 后，若已建立 symlink 则自动生效；否则执行 README 中的 `ln -sf` 命令。
