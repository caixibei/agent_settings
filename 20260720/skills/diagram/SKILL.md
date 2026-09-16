---
name: diagram
description: 图表生成 - 流程图/时序图/思维导图
---

# 图表生成

> **前置依赖**：需要 `superpowers` 插件（brainstorming 技能）和 excalidraw 可视化能力。

## 插件检测

执行前必须确认插件是否可用：
1. 检查当前 session 是否加载了 `superpowers` 相关技能
2. 若未加载，**告知用户**：「需要 superpowers 插件，请先启用 `superpowers@claude-plugins-official`，或使用 Mermaid 语法替代」
3. **禁止**在插件未加载时静默跳过或假装执行

## 使用方式

```text
使用 brainstorming 技能来帮我梳理：<需求描述>，
并使用 excalidraw 以 HTML 方式画出详细的业务流程图、时序图。
```

支持的图表类型：

- 流程图 — 顺序流程、工作流、决策树
- 关系图 — 实体关系、系统组件
- 思维导图 — 概念层次、头脑风暴
- 架构图 — 系统设计、模块交互
- 数据流图（DFD）、泳道图、类图、序列图、ER 图

## 降级方案（插件不可用时）

若 superpowers 不可用：
- 使用 Mermaid 语法生成流程图/时序图（` ```mermaid ` 代码块）
- 使用 `sequentialthinking` MCP 工具梳理逻辑后，用 Mermaid 固化输出
- 将图表以 HTML 文件形式输出，方便留存
