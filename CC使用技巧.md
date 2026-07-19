# Claude Code 使用技巧：插件、MCP 与提示词工程实践

> 作者：蔡熙贝 | 最后更新：2026-07-09

本文记录了作者在实际工程场景中使用 Claude Code 的经验，涵盖插件生态、MCP 工具、提示词组织策略三部分。重点讨论如何在企业级项目中正确配置 Claude Code，使其输出稳定、可预期。

---

## 1. 前置依赖

### 1.1 Bun 运行时

部分插件（如 claude-mem）依赖 Bun 运行时，请提前安装：

```powershell
powershell -c "irm bun.sh/install.ps1 | iex"
```

### 1.2 插件市场安装

复制以下命令发送给 Claude Code，自动完成市场注册：

```text
永久安装：/plugin marketplace add thedotmack/claude-mem
永久安装：/plugin marketplace add anthropics/claude-plugins-official
永久安装：/plugin marketplace add obra/superpowers-marketplace
永久安装：/plugin marketplace add axtonliu/axton-obsidian-visual-skills
```

> 若 `claude-mem` 拉取失败，可执行 `npx claude-mem install` 一键安装。

---

## 2. 插件安装

### 2.1 claude-plugins-official（官方插件集）

推荐指数：⭐⭐⭐⭐⭐

```text
永久安装：/plugin install claude-code-setup@claude-plugins-official --scope user
永久安装：/plugin install claude-md-management@claude-plugins-official --scope user
永久安装：/plugin install frontend-design@claude-plugins-official --scope user
永久安装：/plugin install code-review@claude-plugins-official --scope user
永久安装：/plugin install superpowers@claude-plugins-official --scope user
```

### 2.2 superpowers-marketplace（开发方法论生态）

推荐指数：⭐⭐⭐⭐⭐

```text
永久安装：/plugin install superpowers@superpowers-marketplace --scope user
永久安装：/plugin install claude-session-driver@superpowers-marketplace --scope user
永久安装：/plugin install double-shot-latte@superpowers-marketplace --scope user
永久安装：/plugin install elements-of-style@superpowers-marketplace --scope user
永久安装：/plugin install episodic-memory@superpowers-marketplace --scope user
永久安装：/plugin install private-journal-mcp@superpowers-marketplace --scope user
永久安装：/plugin install superpowers-chrome@superpowers-marketplace --scope user
永久安装：/plugin install superpowers-lab@superpowers-marketplace --scope user
永久安装：/plugin install superpowers-developing-for-claude-code@superpowers-marketplace --scope user
```

### 2.3 claude-mem（项目记忆引擎）

推荐指数：⭐⭐⭐⭐⭐

```text
永久安装：/plugin install claude-mem@claude-mem --scope user
```

**常见问题排查**

**报错：** `Cannot find module 'zod/v3'`

```powershell
cd ~\.claude\plugins\marketplaces\claude-mem\plugin
bun install --registry=https://registry.npmjs.org/ --frozen-lockfile

cd ~\.claude\plugins\marketplaces\claude-mem
npm run worker:restart
```

**报错：** `[INFO][SDK] Not logged in · Please run /login`

在 `~/.claude-mem/settings.json` 中修改配置：

```json
{
  "CLAUDE_MEM_MODEL": "sonnet",
  "CLAUDE_MEM_MODE": "code--zh"
}
```

**注意：** 升级插件后，若设置钩子提示版本不一致，执行 `npx claude-mem repair` 刷新运行时依赖。

### 2.4 claude-mem 关键参数配置

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `CONTEXT_OBSERVATIONS` | 观察记录注入量 | 20 |
| `CONTEXT_FULL_COUNT` | 完整 narrative 注入量 | 3 |
| `CONTEXT_SESSION_COUNT` | 会话摘要注入量 | 5 |
| `SHOW_LAST_MESSAGE` | 是否注入上一会话最后回复 | `false` |

### 2.5 axton-obsidian-visual-skills

推荐指数：⭐⭐⭐⭐

```text
永久安装：/plugin install obsidian-visual-skills --scope user
```

### 2.6 插件市场升级

定期执行以下命令保持市场最新：

```text
/plugin marketplace update claude-plugins-official
/plugin marketplace update claude-mem
/plugin marketplace update superpowers-marketplace
```

---

## 3. MCP 工具

### 3.1 Chrome-Devtools

推荐指数：⭐⭐⭐⭐⭐

Chrome DevTools MCP 通过 Model Context Protocol 将 Chrome 开发者工具暴露给 Claude Code，使其能实时调试网页、分析性能、自动化浏览器操作。

配置路径（Claude Code Desktop）：`%userprofile%\AppData\Local\Claude-3p\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest", "--autoConnect"]
    }
  }
}
```

### 3.2 SequentialThinking

推荐指数：⭐⭐⭐⭐

结构化逐步推理工具，适用于复杂业务逻辑梳理和多条件分支分析。

```json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

---

## 4. Skills 技能清单

以下技能安装路径：`~/.claude/skills`

| 技能 | 推荐指数 | 用途 |
|------|---------|------|
| [superpowers](https://github.com/obra/superpowers/) | ⭐⭐⭐⭐⭐ | 软件开发方法论，脑暴/调试/审查全流程 |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | ⭐⭐⭐⭐⭐ | Anthropic 官方，生成高质量网页 |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | ⭐⭐⭐⭐⭐ | 像专业 Reviewer 一样检查网页质量 |
| [excalidraw-diagram](https://github.com/axtonliu/axton-obsidian-visual-skills) | ⭐⭐⭐⭐ | Excalidraw 图表、Mermaid 流程图、Canvas 思维导图 |
| [html-anything](https://github.com/nexu-io/html-anything) | ⭐⭐⭐ | Markdown 转精美 HTML 页面/海报/卡片 |
| [web-access](https://github.com/eze-is/web-access) | ⭐⭐ | 浏览器自动化（需开启远程调试） |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | ⭐⭐ | 中文去 AI 味，识别空话套话 |
| [ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | ⭐⭐ | 中文文章配图，"小黑"风格插图 |
| [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) | ⭐⭐ | 小红书图文/公众号封面生成 |
| [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | ⭐⭐ | 文章观点转 PPT/演讲图/封面 |
| [khazix-skills](https://github.com/KKKKhazix/khazix-skills) | ⭐⭐ | 万字长文、公众号研究报告 |

---

## 5. 提示词工程：CLAUDE.md 与 Rules 的正确分工

### 5.1 核心认知：完备性不是线性收益

很多人误认为 CLAUDE.md 写得越详细越好。但 LLM 对长指令的遵从遵循 **U 型注意力曲线**：

```
遵从度
  高 ┤ ██                                ██
     │ ██       (中部注意力淹没区)        ██
     │ ██   ████████████████████████     ██
  低 ┤       ████████████████████████████
     └──┬──────┬──────────────────┬─────┬──→ 文档位置
       第1行   中部 30%~70%       末尾  版本记录
```

**关键结论：** 增加规则到某个临界点后，实际遵从度反而下降——新规则不仅自身被忽略，还挤占了已有规则的注意力预算。

根据实际观察，Claude 对 CLAUDE.md 的稳定遵从范围约在 **150～180 行**。超过 200 行后中部规则遵从度显著衰减。

### 5.2 官方建议：总则 + 分流

Claude Code 官方对指令文件的设计意图是：**CLAUDE.md 负责全局上下文，`.claude/rules/` 负责按主题和路径精细化加载。**

```
CLAUDE.md                        .claude/rules/
────────────────                 ─────────────────
全局宪法（<150行）                专项规则（按主题拆分）
• 项目语境                       • annotation.md    （始终加载）
• 交互规范                       • engineering-core.md（始终加载）
• 版本控制纪律                   • pitfalls.md       （始终加载）
• 硬阻断清单                     • frontend.md       （**/*.vue 路径触发）
• Rules 索引（指向 rules/）      • workflows.md       （始终加载）
```

**写进 CLAUDE.md 的条件：** 几乎每次会话都相关、所有人长期遵守的硬性约束。

**拆到 rules/ 的条件：** 仅对某些文件类型或主题生效；或者内容太长不适合常驻主文件。

### 5.3 rules 的最大价值：路径触发

如果 `.claude/rules/frontend.md` 的 frontmatter 带有 `paths` 字段：

```yaml
---
paths:
  - "**/*.vue"
  - "**/*.css"
---
```

则这条规则**仅在 Claude 读取了匹配文件时才进入上下文**。处理 Java 代码时不会背着一整套前端规范——上下文更干净，规则噪音更低。

### 5.4 权衡规则三原则

**原则一：区分"独有规则"与"已知规范"**

```
独有规则（必须写）                已知规范（LLM 已知，可压缩/删除）
──────────────────────           ─────────────────────────────
注释审查计划 + 全方法覆盖          禁止拼接 SQL
TODO 标注 + 废弃注释删除           Controller 不写业务逻辑
强制输出【编辑前检查】模板         异常不能空 catch
Subagent 复查 + 不合格处置        密码不得硬编码
称呼"宗主" + 只读跳过             上传文件校验类型/大小
```

已知规范是 LLM 训练数据中已有的——Claude 不会因为 CLAUDE.md 没写"禁止拼接 SQL"就写出拼接 SQL。这些规则占用 token 但边际遵从增益趋近于零。

**原则二：可执行性 > 陈述完整性**

```
陈述式（低效）                      可执行式（高效）
──────────────────────             ────────────────────────
"禁止拼接 SQL"                      "每次写 SQL 前先 Grep 确认
                                    已有 Mapper XML 的写法"
"异常必须记录日志"                   "catch 块若为空，检查所有
                                    catch (Exception e) {}"
"优先运行相关测试"                   "修改 XxxServiceImpl 后运行
                                    mvn test -pl module -Dtest=XxxServiceTest"
```

陈述式告诉 AI "应该怎样"——它本身就知道。可执行式告诉 AI "具体怎么做"——这才是训练数据里没有的操作上下文。

**原则三：真正的完备 = 规则被遵守的完备**

在 LLM 注意力机制下，完备性和效率不是零和博弈——在一定区间内是正相关的。超过注意力预算的"完备"实际上降低了完备性，因为中部规则形同虚设。

> **切记：真正的优化不是压缩措辞，而是把规则放到它能被真正遵守的位置。**

---

## 6. 技能使用技巧

### 6.0 快捷指令映射：告别复制粘贴

日常高频操作（初始化、脑暴、排查、画图）每次都要复制完整模板，一天十几轮下来非常低效。核心问题在于——你把最常说的信息放在了 LLM 注意力曲线的最低位。

**解决方案：在 CLAUDE.md 中建立"短词 → 长模板"映射表。**

```
用户说             LLM 自动展开为
───────           ──────────────────────────────
初始化             /init 生成项目 CLAUDE.md（≤150行限制）
分析 委托流程       brainstorming 梳理「委托流程」+ companion 草图
排查 NPE           systematic-debugging 逐层溯源 NPE
画图 订单状态       brainstorming + excalidraw 生成订单状态流程图
三步法 定价逻辑     ①脑暴→②推理链→③文档
复盘               修复后同类问题扫描 + 陷阱行追加
提单               Bug 报告标准化：复现→预期→实际→根因→方案
```

**LLM 底层原理：** 短词位于上下文窗口最前端（注意力 U 型曲线最高点），LLM 看到它后立即展开为完整模板——相当于在提示词里装了快捷键。用户侧的 token 开销从每次 50+ 字缩短到 2-4 个字，而 LLM 获取的上下文精度反而更高。

具体实现方式：在 CLAUDE.md 中新增「快捷指令映射」章节，声明短词识别规则和展开行为，LLM 在每次对话加载 CLAUDE.md 时自动获得此能力。

**识别规则：** 短词位于用户消息开头（前 5 个 token 内）即触发。短词后可接具体描述，如 `排查 NullPointerException`。LLM 展开后直接执行，无需回问"是否要启动 XX 模式"——这才是真正的提效。

### 6.1 项目初始化

进入目标项目目录，发送以下指令生成初始 CLAUDE.md（建议控制在 150 行以内）：

```text
请执行 /init 命令生成 CLAUDE.md，必须满足以下硬性约束：
1. 内容范围：仅扫描 src/ 和 lib/ 目录，忽略 tests/、docs/、examples/
2. 篇幅上限：最终输出不超过 150 行
3. 格式要求：每行不超过 25 个汉字，使用清单式写法（禁止长段落）
4. 仅输出以下三类信息：
   - 技术栈（语言、框架、核心依赖，列出 5 项以内）
   - 入口文件与启动命令
   - 所有核心的业务模块及其职责（一句话描述每个模块）
5. 禁止输出：目录树、代码示例、函数签名、API 列表、历史决策记录
如果扫描后内容超出限制，优先保留最高频使用的 20% 信息，其余截断。
```

### 6.2 头脑风暴

```text
使用 brainstorming 技能来帮我梳理这个需求：<需求描述>
```

### 6.3 问题排查

```text
切换到 systematic-debugging 模式来排查问题：<具体问题描述>
```

### 6.4 业务链路可视化

借助 superpowers 技能将梳理思路以图文形式呈现：

```text
使用 brainstorming 技能来帮我梳理：<需求描述>，
并使用可视化 companion 画出当前的业务链路草图，
并使用 excalidraw 生成思维导图、流程图、数据流图、表格时序图
（生成 HTML 文件，文件名以中文命名，方便留存）。
```

### 6.5 图表生成

```text
使用 brainstorming 技能来帮我梳理：<需求描述>，
并使用 excalidraw 以 HTML 方式画出详细的业务流程图、时序图。
```

支持的图表类型：

- 流程图 — 顺序流程、工作流、决策树
- 关系图 — 实体关系、系统组件
- 思维导图 — 概念层次、头脑风暴
- 架构图 — 系统设计、模块交互
- 数据流图（DFD）、泳道图、类图、序列图、ER 图

### 6.6 三步梳理法（复杂业务场景）

对于特别复杂的业务逻辑，推荐使用三步法将 Superpowers 和 SequentialThinking 组合使用：

**第一步：Superpowers 脑暴 — 最大化搜集信息**

```text
使用 superpowers 的 brainstorming 技能，帮我梳理 [具体模块/系统] 的业务逻辑。
```

模型进入发散模式，向你提出关键问题（流程起点和终点？角色参与？异常处理？），引导你补齐信息缺口。

**第二步：SequentialThinking 构建逻辑骨架 — 碎片信息变推理链**

```text
现在，请使用 sequentialthinking 工具，将刚才讨论的所有信息整理成一个
清晰的业务逻辑推理链。请包含主要流程、分支条件、异常处理，
并给出每一步的思考依据。
```

模型生成带编号、可回溯的思维链，每一步都有依据，可随时打断追问。

> **关键点：** SequentialThinking 的精髓在于"每一步都可修正"。如果模型中途问你"是否正确"，请务必正面回答；如果第 3 步不对，直接打断说明实际逻辑，它会基于修正重新生成后续链条。

**第三步：Superpowers 固化输出 — 思维链变可交付文档**

```text
请使用 superpowers 的写作/代码技能，将上一步的思考链，
转化为一份 [业务逻辑说明文档 / 流程图代码 / 接口时序图]。
```

**三步法适用场景速查**

| 场景 | 指令切入点 |
|------|-----------|
| 现有代码太乱，想理清脉络 | `用 sequentialthinking 逆向分析这段代码的业务流程，然后用 superpowers 写出重构建议。` |
| 跨系统交互逻辑梳理 | `用 superpowers 脑暴找出所有交互方，再用 sequentialthinking 画出数据流转的时序步骤。` |
| 梳理完生成可视化图表 | `将 sequentialthinking 生成的步骤，用 superpowers 转化为 Mermaid 流程图代码。` |

### 6.7 验证技能是否加载

若 Claude 直接开始编写代码而未走工作流，可提醒：

```text
请按照 Superpowers 的工作流程，先进行头脑风暴
```

---

## 7. Agent 模式切换

Claude Code 默认采用标准输出样式，另有三种内置样式：

| 样式 | 说明 |
|------|------|
| **Proactive** | 立即执行，基于合理假设推进，减少决策停顿，比自动模式更强自主性 |
| **Explanatory** | 完成任务的同时提供教育性见解，解释方案选择依据和代码库设计模式 |
| **Learning** | 协作式边学边做，Claude 分享见解并邀请你贡献关键代码片段，代码中会添加 `TODO(human)` 标记 |

通过设置文件切换：

```json
{
  "outputStyle": "Learning"
}
```

> 独立的 `/output-style` 命令已在 v2.1.73 中弃用，v2.1.91 移除。

---

## 8. CC-Switch 通用配置参考

避免切换模型时插件配置被清空（参考 cc-switch 官方 issues）：

```json
{
  "enableWorkflows": true,
  "enabledPlugins": {
    "claude-mem@claude-mem": true,
    "claude-code-setup@claude-plugins-official": true,
    "claude-md-management@claude-plugins-official": true,
    "code-review@claude-plugins-official": true,
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "claude-session-driver@superpowers-marketplace": true,
    "double-shot-latte@superpowers-marketplace": true,
    "elements-of-style@superpowers-marketplace": true,
    "episodic-memory@superpowers-marketplace": true,
    "private-journal-mcp@superpowers-marketplace": true,
    "superpowers-chrome@superpowers-marketplace": true,
    "superpowers-developing-for-claude-code@superpowers-marketplace": true,
    "superpowers-lab@superpowers-marketplace": true,
    "superpowers@superpowers-marketplace": true,
    "obsidian-visual-skills@axton-obsidian-visual-skills": true
  },
  "env": {
    "CLAUDE_CODE_ATTRIBUTION_HEADER": 0,
    "CLAUDE_CODE_EFFORT_LEVEL": "max",
    "DISABLE_AUTOUPDATER": "1"
  },
  "extraKnownMarketplaces": {
    "claude-mem": {
      "source": { "repo": "thedotmack/claude-mem", "source": "github" }
    },
    "claude-plugins-official": {
      "source": { "repo": "anthropics/claude-plugins-official", "source": "github" }
    },
    "superpowers-marketplace": {
      "source": { "repo": "obra/superpowers-marketplace", "source": "github" }
    }
  }
}
```
