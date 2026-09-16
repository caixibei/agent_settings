---
name: vue-pitfalls-reference
description: Use as reference when diagnosing Vue, Element UI, table, form, layout, or data-shape issues.
priority: reference
paths: **/*.vue
---

# Vue / Element UI 高风险案例

- `el-select` 自定义 `value-key` 时，值必须是对象且唯一字段稳定；接口返回后若值是字符串而选项是对象会导致回显异常，先确认真实数据形状再改 formatter。
- `vxe-table` 选中行消失通常不是分页问题；确认 `row-id` 是否唯一稳定、`reserve` 是否配置、翻页是否清理选择。
- `this.$set(this.form, 'field', value)` 是 Vue 2 动态字段响应式更新的必要方式。
- 弹窗关闭后 `resetFields()`、表单对象重置和表格选择清理必须与项目现有模式一致。
- 页面分为“列表页 + 新增/编辑弹窗”时，列表负责查询/分页/打开弹窗，弹窗负责字段和提交；不为单页简单表单强行拆分。
- 按钮隐藏、禁用和后端接口鉴权是三件事；前端判断不能替代后端权限校验。
- 导出条件应从列表查询状态生成，不要重新维护第二套筛选状态；导出格式、分页和字段口径必须与业务需求一致。
