---
name: outline-build
description: Orchestrator tool that converts a confirmed story brief into story and episode outlines. Use when user @'s outline-build with brief.md or a project name after the story core is confirmed.
disable-model-invocation: true
---

# Outline Build · 大纲构建工具

## 触发

用户 `@outline-build` 并提供以下任一输入：

| 输入类型 | 示例 |
|----------|------|
| 项目路径 | `projects/商妃/brief.md` |
| 剧名 | `商妃`（自动找 `projects/<剧名>/brief.md`） |
| 粘贴内容 | 完整的故事初稿 markdown |

可选参数（文字中说明即可）：

- 集数：默认 30 集
- 修改意见：「加强第 10–15 集商战线」

## 执行流程

```
[1] 定位并读取 brief.md
      ↓
[2] 加载 drama-outline + hongguo-platform
      ↓
[3] 生成故事大纲 + 分集大纲（含防呆规则）
      ↓
[4] 写入 projects/<剧名>/outline.md
      ↓
[5] 按 drama-qc 自动修复规则自检修订 outline.md
      ↓
[6] 汇报摘要 + 前 3 集大纲
```

### Step 5 · 自检修订

生成后**立即**按 `drama-qc` 防呆规则与自动修复原则检查 `outline.md`，发现问题直接改，无需用户确认。

### Step 1 · 定位输入

优先级：

1. 用户给的 `.md` 路径
2. `projects/<剧名>/brief.md`
3. 用户粘贴的全文

若 brief 不存在 → 提示先运行 `@draft-build`

### Step 2 · 加载子 Skill

必须 Read：

```
hongguo-drama-harness/skills/drama-outline/SKILL.md
hongguo-drama-harness/skills/hongguo-platform/SKILL.md
```

### Step 3 · 生成大纲

- 遵循 `drama-outline` 模板与规则
- 忠于 brief 已确认的故事核
- 默认 30 集分集大纲

### Step 4 · 写入

`projects/<剧名>/outline.md`

### Step 5 · 汇报

1. 故事大纲摘要（200 字内）
2. 前 3 集分集大纲表
3. 逻辑链验证结果
4. 风险提示
5. **下一步**：确认后 → `@episode-build` 或 `@qc-build`

## 不做的事

- ❌ 不修改 brief 已确认的核心设定（除非发现逻辑硬伤，须标注并询问）
- ❌ 不写完整台词剧本
