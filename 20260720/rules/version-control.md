---
description: 版本控制纪律
---

# 版本控制纪律

## Git 只读原则

禁止执行任何会修改仓库状态的 git 命令（add/commit/push/reset/rebase/checkout/merge/branch -d...）。需要检查文件时使用 Read、Grep、Glob 工具。

允许的只读命令：`status`、`diff`、`log`、`show`、`blame`、`branch`（不带 -d/-D）。

- 变更仅保留本地，由用户自行管理版本控制
- 用户说”回退”时，只通过 Edit 撤销本次修改，不覆盖整个文件

## 敏感配置

- 密钥、密码、token、连接串不得写入代码或日志
- 配置示例使用占位符
- 输出敏感数据时必须脱敏

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
