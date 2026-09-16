---
name: database-field-sync
description: Use when synchronizing database field changes across application layers.
priority: high
---

# 版本控制纪律

> 以下规则与 CLAUDE.md §三 一致。本文件补充 DB 字段变更同步详细规范。

## 规则职责边界

- 本文件负责复述 Git 只读与敏感配置边界，并补充数据库字段变更的全链路同步要求。
- 全局 `CLAUDE.md` 负责版本控制总原则；`java/engineering.md` 负责安全编码；本文件不得放宽 Git、敏感信息或数据库一致性约束。
- 本文件的字段同步清单用于补充变更影响检查，不替代业务假设、注释、工程完成检查和交付格式规则。

## Git 只读原则

见 CLAUDE.md §三。允许的只读命令：`status`、`diff`、`log`、`show`、`blame`、`branch`（不带 -d/-D）。

## 敏感配置

见全局 `CLAUDE.md` 及 `java/engineering.md`「安全编码」。配置示例使用占位符，输出敏感数据时脱敏。

## DB 字段变更同步

新增/删除/重命名字段前，确认同步范围：

```text
迁移脚本 → Entity → DTO → Mapper → Service → 前端 → 测试
```

共享 Mapper 新增返回字段时：
1. 检查实体是否有对应字段映射
2. 检查其他调用方是否受影响
3. 注释字段在后续数据装配中的用途
4. 验证空值和历史数据兼容性
