---
name: java-business-annotations
description: Use when modifying business logic in Java, MyBatis XML, or SQL files.
priority: high
paths: **/*.{java,xml,sql}
---

# Java 业务注释规则

- 修改业务方法前先阅读整个方法；修改后审查全部适用业务段落，不只看改动行。
- 先用清晰命名和结构表达含义。仍无法自解释时，注释说明业务目的、数据来源与去向、分支影响或风险约束；禁止翻译代码。
- 历史代码可原位最小修复，不为补注释拆分方法或迁移分层；旧注释失真时同步更新或删除。
- 业务意图无法由代码、数据或用户确认时写 `// TODO: [待确认业务意图]` 并说明待确认项，不得猜测。
- Mapper、DAO、`getById`、`list`、`page`、`select*` 与 MyBatis SQL 的说明必须覆盖：数据来源、业务目的、条件含义、结果用途、空结果语义和循环相关性能意图。
- 复杂条件、阈值、状态转换、异常吞没或转换、字段复制、正则与循环边界应说明业务原因或风险。
- 公开 API 使用 `/** */`；摘要句完整并以句号结束。Javadoc 优先说明 Why，再说明 What；三项及以上枚举使用 `<ul>/<li>`，有序步骤使用 `<ol>/<li>`，代码标识符使用 `{@code}`，可链接类型或方法使用 `{@link}`。

复杂 Java 修改需要时读取 `java/annotation-checklist.md`；Javadoc 模板、正反例、TODO、异常和反模式案例读取 `examples/annotation-example.md`。
