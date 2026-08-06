---
name: java-annotation-checklist
description: Use when reviewing complex business annotations in Java, MyBatis XML, or SQL changes.
priority: normal
paths: **/*.{java,xml,sql}
---

# Java 注释检查清单

复杂修改只需确认以下五项；不要求为简单修改输出固定表格：

- 已阅读目标方法并理解业务目的、数据来源和结果去向。
- 已识别权限、状态、金额、流程、字段复制、空结果或异常等关键段落。
- 每个持久层调用已说明数据来源、条件、用途、空结果和循环性能意图。
- 注释解释业务原因，且与实现一致；历史注释未失真。
- 修改后已复查受影响方法的业务段落，没有为补注释引入无关重构。

文件类型分档：Java、MyBatis XML、SQL 为 A 档；Vue script/template 为 B 档；样式为 C 档；混合改动按最高档执行。同档同文件组、间隔不足 30 分钟的后续编辑可简化为 `✓ 检查通过`。

适用逻辑段落包括：入参与登录上下文、权限/数据范围、查询条件、每次 Mapper/Service/外部调用、批量装配、关键分支、状态/金额/敏感字段、字段复制、排序分页响应、空结果/异常/降级。
