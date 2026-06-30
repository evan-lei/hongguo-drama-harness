# 工具 Skill vs 内容 Skill

Harness 采用**两层架构**：

## 内容 Skill（怎么做）

定义产出模板、规则、质检维度。Agent 按模板生成内容。

| Skill | 产出 |
|-------|------|
| `drama-prompt-enrich` | 故事初稿 `brief.md` |
| `drama-outline` | 故事/分集大纲 `outline.md` |
| `drama-episode` | 分集剧本 `episodes/ep*.md` |
| `drama-qc` | 质检报告 `qc-*.md` |

## 工具 Skill（一键编排）

用户 `@` 工具 Skill 并给输入，Agent **自动加载对应内容 Skill** 执行全流程（读入 → 生成 → 落盘 → 汇报）。

| 工具 Skill | 调用链 | 典型输入 |
|------------|--------|----------|
| `draft-build` | → `drama-prompt-enrich` | 碎片文字 / `.md` |
| `outline-build` | → `drama-outline` | `brief.md` / 剧名 |
| `episode-build` | → `drama-episode` | `outline.md` / 集数范围 |
| `qc-build` | → `drama-qc` | 任意阶段稿件 |

全程叠加 `hongguo-platform` 规范。

**投稿导出**：`python3 scripts/export-batch-upload.py projects/<剧名>` → `upload-batch.txt`（批量上传格式；第零集自动拼装：剧名 + 梗概 + 题材与情绪 + 设定 + 核心设定 + 人物小传 + 剧本大纲）

**`@qc-build` 默认自动修复**：发现必改项直接改源文件，无需用户逐步确认（见 `drama-qc`）。

## 使用示例

```
@draft-build 女保镖伪装保姆潜入豪门，爽文向

@outline-build projects/隐刃/brief.md

@episode-build 隐刃 第1-3集

@qc-build 隐刃 ep1-3
```
