---
name: java-engineering-pitfalls
description: Use when checking Java, database, transaction, performance, concurrency, or legacy-code risks.
priority: reference
paths: **/*.{java,xml,sql}
---

# Java 与数据库高频陷阱速查

- 正向遍历 `list.remove(i)` 会跳项或越界，使用 `Iterator.remove()` 或倒序遍历。
- `@Transactional` 同类 `this.xxx()` 调用会绕过 AOP；但调用无事务注解基础方法不等于事务失效，先确认目标方法注解。
- `Integer` 拆箱前判空；`BigDecimal` 用 `compareTo()`；字符串用 `equals()` 或 `Objects.equals()`。
- `BeanUtils.copyProperties` 可能覆盖 taskId、状态等上下文字段，复制前保存、复制后恢复并说明原因。
- `getOne` 多条会抛异常，使用 `list` 后按业务规则处理；Controller 不得忽略 Service 业务失败而固定返回 success。
- 手写锁定 SELECT 漏列可能结合 `FieldStrategy.IGNORED` 清空字段；优先全字段查询加 `FOR UPDATE`，或只更新目标字段。
- Set 只用于校验，输出按原 List 过滤以保留顺序；`LIKE '%x%'`、大 IN、内存分页和无 EXPLAIN 的索引修改均需明确性能证据。
- JDBC 批量依赖 `rewriteBatchedStatements=true`；循环中的 wrapper、JSON 序列化和 `anyMatch` 常形成 N+1 或 O(N×M)。
- 多行 `FOR UPDATE` 按主键排序；RR 快照读做 check-then-act 可能违反不变量；乐观锁最多重试 3 次。
- CAS 不应过早写终态；锁必须覆盖所有后续写点；补偿回退要区分流程推进前后。
- 只修一个并发触点或只分析一个方法会遗漏跨请求竞争；自定义事务注解行为必须核实。
- 历史代码不因分层重构；防御性止血不等于业务完成，验证标准是操作真正成功。
