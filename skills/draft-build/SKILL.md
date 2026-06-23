---
name: draft-build
description: Orchestrator tool that turns fragmented text or a .md file into a structured 故事初稿. Use when user @'s draft-build with keywords, a one-line idea, or a markdown file path.
disable-model-invocation: true
---

# Draft Build · 故事初稿构建工具

## 触发

用户 `@draft-build` 并提供以下任一输入：

| 输入类型 | 示例 |
|----------|------|
| 简短文字 | 「女保镖伪装保姆潜入豪门，爽文」 |
| 关键词 | 重生、复仇、甜宠 |
| `.md` 文件 | `@ideas/脑洞.md` 或绝对路径 |

## 执行流程（严格按序，不跳步）

```
[1] 解析输入
      ↓
[2] 加载 drama-prompt-enrich + hongguo-platform
      ↓
[3] 生成故事初稿
      ↓
[4] 写入 projects/<剧名>/brief.md
      ↓
[5] 汇报摘要 + 待确认项
```

### Step 1 · 解析输入

- **文件路径** → 用 Read 读取全文，作为碎片输入
- **纯文字** → 直接作为碎片输入
- 从内容推断剧名（简短、无特殊字符）；无法推断时用 `untitled-<YYYYMMDD>`

### Step 2 · 加载子 Skill

必须 Read 以下文件后再生成：

```
hongguo-drama-harness/skills/drama-prompt-enrich/SKILL.md
hongguo-drama-harness/skills/hongguo-platform/SKILL.md
```

（若 symlink 已配置，等价路径：`~/.cursor/skills/drama-prompt-enrich/SKILL.md`）

### Step 3 · 生成故事初稿

- **完全遵循** `drama-prompt-enrich` 的输出模板与丰富规则
- 信息不足时：最多追问 3 个问题，**或**标注「待确认项」后直接生成（工具模式下优先后者，减少打断）
- 产出后对照 `hongguo-platform` 质检速查做一轮自检

### Step 4 · 写入项目

```bash
mkdir -p /Users/user/Documents/hongguo-drama-harness/projects/<剧名>/episodes
```

写入：`projects/<剧名>/brief.md`

### Step 5 · 自检修订

按 `drama-qc` 自动修复规则检查 `brief.md`，发现必改项直接修订，无需用户确认。

### Step 6 · 汇报

向用户呈现：

1. **一句话梗概**
2. **核心人物与反差**（表格摘要）
3. **前 3 集钩子**（表格摘要）
4. **待确认项**（如有）
5. **文件路径**
6. **下一步**：确认故事核后 → `@outline-build`

## 不做的事

- ❌ 不自动进入大纲阶段（除非用户明确要求）
- ❌ 不调用 `drama-outline`（那是下一阶段 `outline-build` 的职责）
- ❌ 不跳过 `drama-prompt-enrich` 模板

## 命名说明

| 术语 | 对应 Skill | 产出文件 |
|------|------------|----------|
| 故事初稿 | `drama-prompt-enrich` | `brief.md` |
| 故事/分集大纲 | `drama-outline` | `outline.md` |

## 示例

**输入**：`穿越成炮灰庶女，用现代商业手段逆袭，甜爽向`

**执行**：解析 → 加载子 Skill → 按模板生成 → 保存 `projects/商妃炮灰庶女的百亿算盘/brief.md` → 汇报摘要
