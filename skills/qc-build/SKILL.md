---
name: qc-build
description: Orchestrator tool that runs structured quality checks on brief, outline, or episode scripts. Use when user @'s qc-build before submission or to validate any draft stage.
disable-model-invocation: true
---

# QC Build · 剧本质检工具

## 触发

用户 `@qc-build` 并提供：

| 输入类型 | 示例 |
|----------|------|
| 项目 + 阶段 | `商妃 brief` / `商妃 outline` / `商妃 ep1-3` |
| 文件路径 | `projects/商妃/brief.md` |
| 粘贴内容 | 任意稿件片段 |

## 执行流程

```
[1] 定位稿件 + 识别阶段（brief / outline / episode）
      ↓
[2] 加载 drama-qc + hongguo-platform
      ↓
[3] 按维度逐项质检
      ↓
[4] 【自动修复】有必改项 → 直接修订源文件（无需用户确认）
      ↓
[5] 复检 → 仍有必改项则继续修（最多 3 轮）
      ↓
[6] 写入 qc 报告（含自动修订记录）
      ↓
[7] 汇报最终结论
```

**默认行为**：发现 🔴 必改项时**不要停下来等用户确认**，按 `drama-qc` 自动修复规则直接改源文件。

### Step 1 · 定位稿件

| 用户说 | 读取 |
|--------|------|
| `brief` / 未指定阶段 | `brief.md` |
| `outline` | `outline.md` |
| `ep` / `episode` / `第N集` | `episodes/ep*.md` |
| 具体路径 | 该文件 |

### Step 2 · 加载子 Skill

必须 Read：

```
hongguo-drama-harness/skills/drama-qc/SKILL.md
hongguo-drama-harness/skills/hongguo-platform/SKILL.md
```

### Step 3 · 质检

- 遵循 `drama-qc` 报告模板
- 必改项必须具体可执行
- 前 3 集相关维度加权

### Step 4 · 自动修复

遵循 `drama-qc`「自动修复」章节：

1. 逐条处理 🔴 必改项，修订 `brief.md` / `outline.md` / `episodes/*.md`
2. 修订后复检；循环直至 ✅ 或触发「需人工决策」（最多 3 轮）
3. 在 qc 报告中记录每条修订的位置与内容

### Step 5 · 写入报告

`projects/<剧名>/qc-<阶段>-<YYYYMMDD>.md`（含「自动修订记录」和「复检结论」）

### Step 6 · 汇报

1. 总结论（✅ / ⚠️ / ❌）——**复检后**的结论
2. 已自动修订项清单（简述）
3. 剩余问题（如有，仅 🟡 建议项或需人工决策项）
4. 下一步建议

## 投稿前建议

完整投稿链路：

```
@draft-build → @outline-build → @qc-build（自动修）→ @episode-build → @qc-build（自动修）
```

`@qc-build` 默认自动修复，无需用户逐步确认必改项。
