# Skill 路线图

## 架构

```
用户 @工具Skill + 输入
        ↓
   工具 Skill（编排：读入 → 调用 → 落盘 → 汇报）
        ↓
   内容 Skill（模板 + 规则）
        ↓
   hongguo-platform（全程规范）
```

## 已完成 ✅

### 内容 Skill

| Skill | 用途 | 产出 |
|-------|------|------|
| `hongguo-platform` | 平台规范、格式、政策、避坑 | — |
| `drama-prompt-enrich` | 碎片想法 → 故事初稿 | `brief.md` |
| `drama-outline` | 初稿 → 故事大纲 + 分集大纲 | `outline.md` |
| `drama-episode` | 大纲 → 标准格式分集剧本 | `episodes/ep*.md` |
| `drama-qc` | 剧本质检 checklist | `qc-*.md` |

### 工具 Skill

| Skill | 调用 | 典型输入 |
|-------|------|----------|
| `draft-build` | `drama-prompt-enrich` | 碎片文字 / `.md` |
| `outline-build` | `drama-outline` | `brief.md` / 剧名 |
| `episode-build` | `drama-episode` | `outline.md` / 集数 |
| `qc-build` | `drama-qc` | 任意阶段稿件 |

## 规划中 📋

| Skill | 用途 | 依赖 |
|-------|------|------|
| `drama-genre` | 题材库 + 爆款结构模式 | 选题阶段，可嵌入 `draft-build` |
| `drama-pull` | 拉片拆解辅助 | 学习/Reference |

## 工作流原则

1. **分层产出**：初稿 → 大纲 → 分集稿，不跳步
2. **工具编排**：用户 `@` 工具 Skill，Agent 自动链式调用内容 Skill
3. **自动质检修复**：`@qc-build` 发现必改项直接改源文件，无需用户逐步确认（见 `drama-qc`）
4. **人机分工**：AI 扩写与润色，人把控故事核与关键转折
5. **版本留存**：`projects/<剧名>/` 下保留每版迭代

## 推荐流水线

```
@draft-build <想法>
    → 确认故事核
@outline-build <剧名>
    → 确认大纲
@episode-build <剧名> 第1-3集
    → 打磨前 3 集
@qc-build <剧名> ep1-3
    → 修改 → 再 qc → 投稿
```
