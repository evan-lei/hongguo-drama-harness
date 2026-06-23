# hongguo-drama-harness

红果短剧剧本创作的 Harness 体系：用 Cursor Skills + Prompt 模板，把「碎片想法」稳定转化为可投稿的剧本资产。

## 仓库用途

| 目录 | 说明 |
|------|------|
| `skills/` | Cursor Agent Skills（平台规范、Prompt 丰富、后续分集/质检等） |
| `prompts/` | 可复用的 Prompt 片段与版本记录 |
| `projects/` | 具体剧本项目（每部剧一个子目录，含故事初稿、大纲、分集稿） |

## Harness 流水线

两层架构：**工具 Skill**（用户 `@` 触发）编排 **内容 Skill**（模板与规则）。

```
@draft-build <碎片想法|.md>  → brief.md
@outline-build <剧名>        → outline.md
@episode-build <剧名> 第1-3集 → episodes/ep*.md
@qc-build <剧名>             → qc-*.md
         → 红果创服平台投稿
```

全程遵守 `hongguo-platform`。详见 [skills/tools/README.md](skills/tools/README.md)。

## 本地使用

将 skills 链接到 Cursor 个人技能目录（一次性）：

```bash
HARNESS=/Users/user/Documents/hongguo-drama-harness/skills
SKILLS=~/.cursor/skills

ln -sf $HARNESS/hongguo-platform $SKILLS/hongguo-platform
ln -sf $HARNESS/drama-prompt-enrich $SKILLS/drama-prompt-enrich
ln -sf $HARNESS/drama-outline $SKILLS/drama-outline
ln -sf $HARNESS/drama-episode $SKILLS/drama-episode
ln -sf $HARNESS/drama-qc $SKILLS/drama-qc
ln -sf $HARNESS/draft-build $SKILLS/draft-build
ln -sf $HARNESS/outline-build $SKILLS/outline-build
ln -sf $HARNESS/episode-build $SKILLS/episode-build
ln -sf $HARNESS/qc-build $SKILLS/qc-build
```

用法：在对话中 `@draft-build` 并给出想法，例如：

> `@draft-build` 女保镖伪装保姆潜入豪门，爽文向

## 相关链接

- GitHub: https://github.com/evan-lei/hongguo-drama-harness
- 红果短剧创作服务平台: https://www.douyin.com（搜索「红果短剧创作服务平台」进入官方入口）
- 平台开放个人编剧入驻（2025.11 起）

## Skill 路线图

见 [ROADMAP.md](ROADMAP.md)。
