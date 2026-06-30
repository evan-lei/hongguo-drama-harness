---
name: episode-build
description: Orchestrator tool that expands episode outlines into standard 红果短剧 episode scripts. Use when user @'s episode-build with outline.md, a project name, or an episode range like 第1-3集.
disable-model-invocation: true
---

# Episode Build · 分集剧本构建工具

## 触发

用户 `@episode-build` 并提供：

| 输入类型 | 示例 |
|----------|------|
| 项目 + 集数 | `商妃 第1-3集` |
| 文件路径 | `projects/商妃/outline.md` |
| 仅剧名 | `商妃`（默认生成第 1–3 集） |

## 执行流程

```
[1] 定位 outline.md + 确认集数范围
      ↓
[2] 加载 drama-episode + hongguo-platform
      ↓
[3] 逐集生成分集剧本
      ↓
[4] 写入 projects/<剧名>/episodes/ep<N>.md
      ↓
[5] 汇报 + 建议质检
```

### Step 1 · 定位输入

- `projects/<剧名>/outline.md` 必须存在；否则提示先 `@outline-build`
- 集数范围：未指定 → 第 1–3 集；支持 `第N集` / `第A-B集`

### Step 2 · 加载子 Skill

必须 Read：

```
hongguo-drama-harness/skills/drama-episode/SKILL.md
hongguo-drama-harness/skills/hongguo-platform/SKILL.md
```

### Step 3 · 生成剧本

- 遵循 `drama-episode` 格式与规则
- **正文字数**：每集 **600–900 汉字**（创服硬性要求 300–2500）
- 逐集生成，不合并到一个文件
- 写完后逐集统计汉字数；不足 300 **自动扩写**，超过 2500 **自动删减**

### Step 4 · 写入

```
projects/<剧名>/episodes/ep1.md
projects/<剧名>/episodes/ep2.md
...
```

### Step 5 · 自动质检修订

生成每集后，按 `drama-qc` 自动修复规则检查并修订当集剧本；全部批次写完后对 `episodes/` 做一轮 qc 修订。

### Step 6 · 汇报

1. 已生成集数与文件路径
2. 每集一句话摘要 + 结尾卡点
3. 篇幅自检结果
4. 批量上传：运行 `export-batch-upload.py` 生成 `upload-batch.txt`（第零集自动拼装：梗概 + 题材与情绪 + 设定 + 核心设定 + 人物 + 大纲）
5. **下一步**：`@qc-build` 自动修订，或投稿创服批量上传

## 不做的事

- ❌ 不擅自改大纲情节点
- ❌ 不默认一次生成全剧 30 集（除非用户明确要求）
