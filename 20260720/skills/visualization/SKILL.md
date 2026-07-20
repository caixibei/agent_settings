---
name: visualization
description: 业务链路可视化 - 脑暴+图表
---

# 业务链路可视化

> **前置依赖**：需要 `superpowers` 插件（brainstorming 技能）和 excalidraw 可视化能力。

## 插件检测

执行前必须确认插件是否可用：
1. 检查当前 session 是否加载了 `superpowers` 相关技能
2. 若未加载，**告知用户**：「需要 superpowers 插件，请先启用 `superpowers@claude-plugins-official`，或使用 `/brainstorming` 和 `/diagram` 替代」
3. **禁止**在插件未加载时静默跳过或假装执行

## 使用方式

借助 superpowers 技能将梳理思路以图文形式呈现：

```text
使用 brainstorming 技能来帮我梳理：<需求描述>，
并使用可视化 companion 画出当前的业务链路草图，
并使用 excalidraw 生成思维导图、流程图、数据流图、表格时序图
（生成 HTML 文件，文件名以中文命名，方便留存）。
```

## 降级方案（插件不可用时）

若 superpowers 不可用，使用以下替代方案：
- 用 `sequentialthinking` MCP 工具梳理业务逻辑链路
- 用 Mermaid 语法在 Markdown 中生成流程图
- 用 `mcp__chrome-devtools__evaluate_script` 在浏览器中渲染简单图表
