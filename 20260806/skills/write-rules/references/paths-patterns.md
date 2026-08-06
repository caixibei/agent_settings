# 规则的路径模式

## 基础模式

| 模式 | 说明 | 匹配示例 |
|---------|-------------|---------------|
| `*` | 当前目录任意文件 | `*.ts` 匹配 `index.ts` |
| `**` | 任意目录深度 | `**/*.ts` 匹配 `src/utils/helper.ts` |
| `?` | 单个字符 | `file?.ts` 匹配 `file1.ts` |

## 目录模式

```yaml
# 某目录下所有文件
paths: src/api/**

# 仅直接子级
paths: src/api/*

# 特定子目录结构
paths: src/**/utils/**
```

## 扩展名模式

```yaml
# 单扩展名
paths: **/*.ts

# 多扩展名（花括号展开）
paths: **/*.{ts,tsx}

# 排除测试文件（改用独立规则）
paths: src/**/*.ts
# 然后为测试单独建规则
paths: **/*.test.ts
```

## 多路径模式

```yaml
# 逗号分隔
paths: src/**/*.ts, lib/**/*.ts

# 目录花括号展开
paths: {src,lib,packages}/**/*.ts
```

## 常见配置

### 前端项目

```yaml
# 组件
paths: src/components/**/*.{tsx,jsx}

# 样式
paths: src/**/*.{css,scss,less}

# 状态管理
paths: src/store/**/*.ts
```

### 后端项目

```yaml
# API 路由
paths: src/api/**/*.ts, src/routes/**/*.ts

# 数据库
paths: src/db/**/*.ts, src/models/**/*.ts

# 中间件
paths: src/middleware/**/*.ts
```

### Monorepo

```yaml
# 特定包
paths: packages/core/**/*.ts

# 所有包
paths: packages/**/src/**/*.ts

# 共享代码
paths: {packages,libs}/shared/**/*.ts
```

### 测试规则

```yaml
# 所有测试文件
paths: **/*.test.ts, **/*.spec.ts

# 特定测试目录
paths: tests/**/*.ts, __tests__/**/*.ts

# 仅 E2E 测试
paths: e2e/**/*.ts, cypress/**/*.ts
```

## 优先级说明

- 更具体的路径优先级更高
- 无 `paths:` 的规则为全局（优先级最低）
- 文件名要达意：`api-conventions.md`、`testing-guidelines.md`
