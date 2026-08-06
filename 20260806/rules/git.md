---
name: git-version-control
description: Use when inspecting repository state or protecting local changes and sensitive files.
priority: critical
---

# Git 与版本控制

- 禁止执行任何 Git 写命令；只允许 `status`、`diff`、`log`、`show`、`blame`、`branch` 等只读检查。
- 变更仅保留本地，由用户自行进行版本控制；用户说“回退”时，通过 Edit 撤销本次修改，不回退整个文件。
- 配置、密钥、token、连接信息、`.env`、凭据和个人数据不得写入代码、规则或版本库；输出时脱敏。
- 不为验证或排查绕过 hook、权限或安全检查，不执行破坏性清理、强制推送、reset、restore、checkout 或删除分支。

## 数据库字段同步

新增、删除或重命名字段前，核对：迁移脚本 → Entity → DTO → Mapper → Service → 前端 → 测试。

共享 Mapper 新增返回字段时：

1. 确认实体存在正确字段映射。
2. 检查其他调用方是否受影响。
3. 说明字段在后续数据装配中的用途。
4. 验证空值和历史数据兼容性。
