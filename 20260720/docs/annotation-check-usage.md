# 注释审查强化方案 - 使用说明

## 方案概述

本方案通过三种机制强制执行注释审查：
1. **`/annotation-check` 命令** - 手动触发注释审查
2. **PreToolUse hook** - 在 Edit/Write 前自动拦截
3. **CLAUDE.md 规则** - 明确强制要求

## 已完成的配置

### 1. 创建了 `/annotation-check` 命令

**文件位置：** `~/.claude/commands/annotation-check.md`

**使用方法：**
```
/annotation-check
```

**触发时机：** 每次修改业务代码前必须执行

### 2. 配置了 PreToolUse hook

**文件位置：** `~/.claude/settings.json`

**配置内容：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚠️ 警告：请先执行 /annotation-check 命令进行注释审查，然后再修改代码。'"
          }
        ]
      }
    ]
  }
}
```

**效果：** 每次调用 Edit 或 Write 工具时，会自动显示警告信息

### 3. 修改了 CLAUDE.md 规则

**文件位置：** `~/.claude/CLAUDE.md`

**新增内容：** 在"四、编辑前硬规则"中添加了"4.0 强制注释审查（必须执行）"

## 使用流程

### 标准流程

```
1. 用户提出修改需求
2. Claude 输出检查清单（调用 /annotation-check）
3. Claude 审查全方法业务逻辑段落
4. Claude 按照注释内容维度覆盖
5. Claude 执行编辑后复查（DoD）
6. Claude 修改代码并添加注释
7. 验证注释已写入文件
```

### 强制执行机制

**机制1：手动触发**
```bash
# 在对话中输入
/annotation-check
```

**机制2：自动拦截**
- 每次调用 Edit 或 Write 工具时，会自动显示警告信息
- 警告信息：`⚠️ 警告：请先执行 /annotation-check 命令进行注释审查，然后再修改代码。`

**机制3：规则要求**
- CLAUDE.md 明确要求：`未执行注释审查，禁止修改代码。`

## 验证方法

### 验证1：检查命令是否存在
```bash
ls ~/.claude/commands/annotation-check.md
```

### 验证2：检查 hook 配置
```bash
cat ~/.claude/settings.json | grep -A 10 "hooks"
```

### 验证3：检查 CLAUDE.md 规则
```bash
grep -A 20 "4.0 强制注释审查" ~/.claude/CLAUDE.md
```

## 常见问题

### Q1：为什么需要执行注释审查？

**A：** 为了确保：
1. 代码修改符合业务注释规范
2. 注释解释了"为什么存在、数据从哪来、处理后到哪里去"
3. 数据库调用有完整的注释说明
4. 避免"欺骗"用户已完成注释审查

### Q2：如果不执行注释审查会怎样？

**A：** 会有以下拦截机制：
1. PreToolUse hook 会显示警告信息
2. CLAUDE.md 规则要求：`未执行注释审查，禁止修改代码`
3. 用户可以拒绝执行 Edit/Write 操作

### Q3：如何确保注释审查被正确执行？

**A：** 可以通过以下方式验证：
1. 检查是否输出了检查清单
2. 检查是否审查了全方法业务逻辑段落
3. 检查是否按照注释内容维度覆盖
4. 检查是否执行了编辑后复查（DoD）
5. 检查注释是否已写入文件

## 总结

本方案通过三种机制强制执行注释审查：
1. **`/annotation-check` 命令** - 提供手动触发方式
2. **PreToolUse hook** - 在 Edit/Write 前自动拦截
3. **CLAUDE.md 规则** - 明确强制要求

**核心原则：** 未执行注释审查，禁止修改代码。

**效果：** 确保每次修改业务代码时，都会按照 annotation.md 规范添加完整的业务注释。
