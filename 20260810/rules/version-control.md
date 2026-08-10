---
description: 版本控制纪律
priority: high
author: 蔡熙贝
---

# 版本控制纪律

> 以下规则与 CLAUDE.md §三 一致。本文件补充 DB 字段变更同步详细规范。

## Git 只读原则

见 CLAUDE.md §三。允许的只读命令：`status`、`diff`、`log`、`show`、`blame`、`branch`（不带 -d/-D）。

## 敏感配置

见 CLAUDE.md §三及 engineering-core.md「安全编码」。配置示例使用占位符，输出敏感数据时脱敏。

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
