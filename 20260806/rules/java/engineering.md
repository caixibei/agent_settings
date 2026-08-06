---
name: java-engineering
description: Use when modifying Java, MyBatis XML, or SQL code.
priority: high
paths: **/*.{java,xml,sql}
---

# Java、MyBatis 与 SQL 工程约束

- SQL 使用 MyBatis `#{}` 或参数化查询；系统边界校验输入；权限、敏感信息、上传和 HTML 输出遵循安全边界。
- 新增事务放在 Service，事务覆盖完整业务操作；checked exception 需要回滚时声明 `rollbackFor = Exception.class`。事务内避免邮件、第三方调用和长耗时操作；空集合不得进入 `<foreach>`。
- 循环内数据库或远程调用先评估 N+1；可批量时收集业务键、一次查询并按归属键建 Map。性能优化不得改变权限、过滤、排序或总数口径。
- 新增能力遵循 Controller → Service → Mapper/DAO → DB；跨模块经目标模块 Service。历史 Controller 可原位最小修复，不因分层形式重构。
- 查询或导出变更时定位真实导出接口，对照条件和字段映射。
- 先读后写按冲突和一致性选择 `FOR UPDATE`、version CAS 或跨服务 Redis 锁；RR 下需最新数据使用锁定读。高风险并发修改才要求时序、EXPLAIN、索引、持锁时间和方案比较。
- DML WHERE 必须有可用索引；多行锁按主键排序；乐观锁验证 `@Version`、拦截器和非空历史 version；锁范围覆盖全部写点；事务注解方法经代理调用。
- 完成前确认业务边界、权限状态金额、N+1、导出路径、引用、并发索引与验证结果。

完整工程矩阵、并发防护清单和历史陷阱按需读取 `examples/pitfalls.md` 与 `core/business-assumptions.md`。
