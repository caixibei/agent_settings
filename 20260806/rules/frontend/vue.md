---
name: vue-engineering
description: Use when modifying Vue components, templates, scripts, or frontend interactions.
priority: high
paths: **/*.vue
---

# Vue 工程规则

- 修改 script 或业务函数时，确认请求参数来源、返回结果去向、校验、权限、状态变化和请求依赖；简单模板绑定无需额外注释。
- Vue 2 动态数组或对象属性使用 `this.$set`；弹窗关闭清理表单和校验；表格刷新评估选择状态；`vxe-table` 使用稳定唯一 `row-id`。
- 查询、重置、分页、排序使用同一接口和参数口径；无依赖请求可并行，有依赖请求必须等待。
- 保持现有 Vue 与 Element 技术栈；表单用 `el-form`，复杂表格用 `vxe-table`，简单列表用 `el-table`，编辑弹窗用 `el-dialog` 与 `el-form`。
- 弹窗、抽屉、复杂表单、跨两个以上页面复用区块和独立选项卡面板按组件边界拆分；简单查询区、页面独有轻量逻辑和历史修复可留在主页面。
- 父子组件使用 props / `$emit`；可编辑表格编码展示问题先验证数据和 API，只在展示层修复。

布局与样式读取 `frontend/css.md`；Vue 案例读取 `frontend/pitfalls.md`；业务注释读取 `java/annotation.md`。
