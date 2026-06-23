# hongguo-drama-harness

红果短剧剧本创作的 Harness 体系：用 Cursor Skills + Prompt 模板，把「碎片想法」稳定转化为可投稿的剧本资产。

## 仓库用途

| 目录 | 说明 |
|------|------|
| `skills/` | Cursor Agent Skills（平台规范、Prompt 丰富、后续分集/质检等） |
| `prompts/` | 可复用的 Prompt 片段与版本记录 |
| `projects/` | 具体剧本项目（每部剧一个子目录，含故事初稿、大纲、分集稿） |

## Harness 流水线

```
碎片想法 → [drama-prompt-enrich] 故事初稿
         → [drama-outline] 故事/分集大纲（规划中）
         → [drama-episode] 分集剧本（规划中）
         → [drama-qc] 质检（规划中）
         → 红果创服平台投稿
```

全程遵守 `hongguo-platform` 的平台要求与避坑清单。

## 本地使用

将 skills 链接到 Cursor 个人技能目录（一次性）：

```bash
ln -sf /Users/user/Documents/hongguo-drama-harness/skills/hongguo-platform ~/.cursor/skills/hongguo-platform
ln -sf /Users/user/Documents/hongguo-drama-harness/skills/drama-prompt-enrich ~/.cursor/skills/drama-prompt-enrich
```

在对话中提及「红果短剧」「故事初稿」「丰富 prompt」等关键词，Agent 会自动加载对应 Skill。

## 相关链接

- GitHub: https://github.com/evan-lei/hongguo-drama-harness
- 红果短剧创作服务平台: https://www.douyin.com（搜索「红果短剧创作服务平台」进入官方入口）
- 平台开放个人编剧入驻（2025.11 起）

## Skill 路线图

见 [ROADMAP.md](ROADMAP.md)。
