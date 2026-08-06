---
name: task-routing
description: Use when classifying task risk and selecting the required development workflow.
priority: critical
---

# 开发工作流

> 决策优先级见 CLAUDE.md §二。
> 工程规范见 `java/engineering.md`；设计模式见 `core/design-principles.md`；注释标准见 `java/annotation.md`；陷阱见 `examples/pitfalls.md`。

## 规则职责边界

- 本文件是任务路由、设计前门控边界、修改后影响面审查和交付入口的主规则。
- `java/annotation.md`、`java/engineering.md`、`core/business-assumptions.md`、`frontend/vue.md`、`core/design-principles.md`、`core/version-control.md` 和 `core/subagent.md` 分别定义各自领域的具体约束；本文件负责安排何时检查，不替代这些规则。
- `examples/pitfalls.md` 提供案例提醒，`examples/delivery.md` 负责最终输出结构；本文件的流程要求不得削弱专业规则，也不得把案例或交付格式当成新的业务约束。

## 核心原则

- 一次只解决已确认的问题
- 历史代码默认最小修复，不顺手做架构重构
- 新增代码优先采用设计模式和组件化
- 修改方法后必须执行全方法业务注释复查
- **每次代码编辑后必须执行影响面审查**，确认修改不波及无关功能
- 无验证证据时不得声明完成
- **设计前 HARD-GATE**：新增能力、跨模块变更，或涉及权限、金额、状态、审批、事务边界、数据结构的修改，必须先呈现设计并获得用户批准；已定位根因且不涉及上述业务假设的局部 Bug，先输出简短方案和影响范围后可直接执行。详细设计前流程见 `development-workflows` 技能。

## 流程路由

| 场景 | 详细规范 | 说明 |
|------|---------|------|
| Bug 修复 | `development-workflows` 技能 | 复现 -> 三步分析（追踪->诊断->修复） -> 注释复查 -> 验证 -> 相邻回归 |
| 新增功能 | `development-workflows` 技能 | 需求理解 -> 业务规则确认 -> 影响分析 -> 接口设计 -> 实现 -> 注释 -> 测试 |
| 设计前流程 | `development-workflows` 技能 | 探索 -> 澄清 -> 方案 -> 呈现设计 -> 批准（HARD-GATE） |
| 代码审查 | `code-review` 技能 | 按严重级别分类，逐维度审查 |
| 交付 | `examples/delivery.md` | 标准交付结构模板 |
| 前端性能（页面无响应/卡顿） | `browser-perf-debug` 技能 | Trace + HAR 数据驱动 -> 定位瓶颈 -> 绕过决策树 -> 优化 |
| 图表与可视化 | `development-workflows` 技能 | 首选 archify，降级 excalidraw/Mermaid |

各场景的详细执行步骤、强制协议（三步分析、业务规则确认、HARD-GATE、阻断升级等）见 `development-workflows` 技能，按需加载。

## 修改后影响面审查（强制）

**每次代码编辑完成后，必须执行一次影响面审查，确认本次修改不会波及无关功能。**

### 触发时机

- Bug 修复的 Edit/Write 完成后
- 新增功能的 Edit/Write 完成后
- 任何涉及共享类、共享注解、共享 Service 的修改后

### 审查内容

1. **共享依赖检查**：修改的类/注解/接口是否被其他模块引用（grep 类名、注解名、方法名）
2. **调用链覆盖**：同一方法是否在其他 Service 中有平行实现（如同名 compare 方法）
3. **注解传播**：修改注解值后，所有使用该注解的代码路径是否都能正确处理新值
4. **数据流完整性**：修改字段映射/转换逻辑后，前端赋值、后端装配、导出、邮件通知等全链路是否一致

### 审查方法

Grep 修改的类名/注解名 -> 逐个确认引用方是否需要同步修改 -> 需要改的立即补充，不需要的记录排除理由。

### 与 `code-review` 技能的关系

轻量自查（每次 Edit 后）聚焦「是否波及无关功能」；`code-review` 技能（交付前）按 CRITICAL/MAJOR/MINOR 逐维度审查。

### 与 `java/engineering.md`「修改后全方法审查」的关系

两者互补，均需执行，聚焦不同：
- **本审查（影响面）**：聚焦跨方法/跨模块，确认修改不波及无关功能。
- **全方法审查**：聚焦方法内，审查被修改方法的全部业务逻辑段落，见 `java/engineering.md`「修改后全方法审查」。

### 多模型交叉审查（可选）

复杂修改（并发控制、事务重构、核心业务逻辑）可邀请其他模型审查同一修改，交叉验证发现遗漏问题。作为轻量自查的补充，非强制。

## 历史代码修改

允许原位修复的场景及处理要求见 `java/engineering.md`「渐进式架构治理」。核心：保持业务结果、控制最小范围、补齐注释、不因分层问题扩大重构。

## 交付要求

> 详细模板见 `examples/delivery.md`。

交付必须包含：
- 根因或需求实现说明
- 修改文件和业务影响
- 验证命令、结果或环境阻断
- 未处理风险
- 一条本次业务注释示例
