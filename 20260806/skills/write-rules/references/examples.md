# 按领域的规则示例

> **说明**：规则文件用于约定/规范。不可变的核心总纲（决策优先级、语言规则等）写在 CLAUDE.md，不写在这里。

## 代码风格约定

### TypeScript（全局）

```yaml
# .claude/rules/typescript.md
---
paths: **/*.{ts,tsx}
---

# TypeScript 规则

- 使用 strict 模式
- 禁止无理由的 any
- 对象类型优先用 interface 而非 type
- 使用具名导出
```

### Python（全局）

```yaml
# .claude/rules/python.md
---
paths: **/*.py
---

# Python 规则

- 遵循 PEP 8
- 公开函数必须加类型标注
- 模块和类必须有 docstring
- 路径用 pathlib 而非 os.path
```

---

## 领域专用规则

### API 端点

```yaml
# .claude/rules/api/validation.md
---
paths: src/api/**/*.ts, src/routes/**/*.ts
---

# API 规则

- 所有端点必须校验入参
- 使用标准错误响应格式
- 必须包含 OpenAPI 文档
- 公开端点必须限流
```

### 数据库操作

```yaml
# .claude/rules/database/safety.md
---
paths: src/db/**/*.ts, src/models/**/*.ts
---

# 数据库规则

- 所有查询必须参数化
- 多步操作必须用事务
- 应用代码中禁止裸 SQL
- 迁移脚本必须可回滚
```

### React 组件

```yaml
# .claude/rules/frontend/components.md
---
paths: src/components/**/*.tsx
---

# 组件规则

- 一文件一组件
- 必须定义 Props interface
- 禁止内联样式
- 必须加无障碍属性
```

---

## 测试规则

### 测试覆盖

```yaml
# .claude/rules/testing/coverage.md
---
paths: **/*.test.ts, **/*.spec.ts
---

# 测试规则

- 覆盖率必须 > 80%
- 主分支禁止跳过测试
- 测试名必须描述行为
- 每个测试聚焦一个断言
```

### E2E 测试

```yaml
# .claude/rules/testing/e2e.md
---
paths: e2e/**/*.ts, cypress/**/*.ts
---

# E2E 规则

- 测试必须独立
- 选择器用 data-testid
- 运行后清理测试数据
- 禁止硬编码超时
```

---

## 安全规则

### 认证

```yaml
# .claude/rules/security/auth.md
---
paths: src/auth/**/*.ts, src/middleware/auth*.ts
---

# 认证规则

- 禁止记录凭据
- token 必须有过期时间
- 使用安全 cookie 标志
- 认证端点必须限流
```

### 密钥

```yaml
# .claude/rules/security/secrets.md
---
# 全局
---

# 密钥规则

- 禁止提交 .env 文件
- 禁止硬编码密钥
- 使用环境变量
- 定期轮换密钥
```

---

## 工作流规则

### Git 约定

```yaml
# .claude/rules/git.md
---
# 全局
---

# Git 规则

- 使用约定式提交信息
- 禁止强推 main/master
- PR 必须经过审查
- 优先 squash merge
```
