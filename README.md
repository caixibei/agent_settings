# agent_settings

[![Claude Code](https://img.shields.io/badge/Claude_Code-%E8%A7%84%E5%88%99%E5%BF%AB%E7%85%A7-d97757?logo=anthropic&logoColor=white)](https://github.com/caixibei/agent_settings/tree/20260920)
[![Codex](https://img.shields.io/badge/Codex-%E9%85%8D%E7%BD%AE%E5%BF%AB%E7%85%A7-10a37f?logo=openai&logoColor=white)](https://github.com/caixibei/agent_settings/tree/20260920)
[![ZCode](https://img.shields.io/badge/ZCode-%E9%85%8D%E7%BD%AE%E5%BF%AB%E7%85%A7-4C8BF5)](https://github.com/caixibei/agent_settings/tree/20260920)

[![Release](https://img.shields.io/github/v/release/caixibei/agent_settings?label=Release)](https://github.com/caixibei/agent_settings/releases)
[![发布日期](https://img.shields.io/github/release-date/caixibei/agent_settings?label=%E5%8F%91%E5%B8%83%E6%97%A5%E6%9C%9F)](https://github.com/caixibei/agent_settings/releases)
[![日期分支](https://img.shields.io/github/branches/caixibei/agent_settings?label=%E6%97%A5%E6%9C%9F%E5%88%86%E6%94%AF)](https://github.com/caixibei/agent_settings/branches)

[![Star](https://img.shields.io/github/stars/caixibei/agent_settings?style=social&label=Star)](https://github.com/caixibei/agent_settings/stargazers)
[![Fork](https://img.shields.io/github/forks/caixibei/agent_settings?style=social&label=Fork)](https://github.com/caixibei/agent_settings/network/members)
[![Watch](https://img.shields.io/github/watchers/caixibei/agent_settings?style=social&label=Watch)](https://github.com/caixibei/agent_settings/watchers)
[![贡献者](https://img.shields.io/github/contributors/caixibei/agent_settings?label=%E8%B4%A1%E7%8C%AE%E8%80%85)](https://github.com/caixibei/agent_settings/graphs/contributors)

[![总提交](https://img.shields.io/github/commit-activity/t/caixibei/agent_settings?label=%E6%80%BB%E6%8F%90%E4%BA%A4)](https://github.com/caixibei/agent_settings/commits/20260920)
[![月提交](https://img.shields.io/github/commit-activity/m/caixibei/agent_settings?label=%E6%9C%88%E6%8F%90%E4%BA%A4)](https://github.com/caixibei/agent_settings/commits/20260920)
[![最近提交](https://img.shields.io/github/last-commit/caixibei/agent_settings/20260920?label=%E6%9C%80%E8%BF%91%E6%8F%90%E4%BA%A4)](https://github.com/caixibei/agent_settings/commits/20260920)
[![Issues](https://img.shields.io/github/issues/caixibei/agent_settings?label=Issues)](https://github.com/caixibei/agent_settings/issues)
[![PR](https://img.shields.io/github/issues-pr/caixibei/agent_settings?label=PR)](https://github.com/caixibei/agent_settings/pulls)
[![仓库体积](https://img.shields.io/github/repo-size/caixibei/agent_settings?label=%E4%BB%93%E5%BA%93%E4%BD%93%E7%A7%AF)](https://github.com/caixibei/agent_settings)
[![代码体积](https://img.shields.io/github/languages/code-size/caixibei/agent_settings?label=%E4%BB%A3%E7%A0%81%E4%BD%93%E7%A7%AF)](https://github.com/caixibei/agent_settings)

Claude Code、Codex、ZCode 三套 AI 编码工具的提示词进化档案。从 2026-07-20 起，每轮配置演进打一个日期分支：CLAUDE.md、AGENTS.md、rules、skills、hooks、commands、settings 当天的全量样子原样入库。分支名就是版本号，相邻两个分支一 diff，就能看到这段时间提示词到底改了什么。

## 时间线

| 分支 | 内容 | 里程碑 |
|---|---|---|
| [20260720](https://github.com/caixibei/agent_settings/tree/20260720) | CLAUDE.md、9 条 rules、skills、hooks、commands、output-styles、settings.json | 第一份完整的 Claude Code 规则体系 |
| [20260804](https://github.com/caixibei/agent_settings/tree/20260804) | rules 目录单独重写 | 规则文本第一次集中打磨 |
| [20260806](https://github.com/caixibei/agent_settings/tree/20260806) | 全套重组：CLAUDE.md + 6 个子目录（138 个文件） | 目录结构定型 |
| [20260810](https://github.com/caixibei/agent_settings/tree/20260810) | 收敛为 CLAUDE.md + rules + settings.json | 做减法：只留生效的部分 |
| [20260820](https://github.com/caixibei/agent_settings/tree/20260820) | skills 体系回归（含 docx/xlsx 等 office skills），打出 Claude规则文档-v26.0819.zip | 开始按版本号打包 |
| [20260821](https://github.com/caixibei/agent_settings/tree/20260821) | claude-code规则及配置.zip 单包（5.4 MB） | 首次单包归档 |
| [20260831](https://github.com/caixibei/agent_settings/tree/20260831) | claude-code 与 codex 双 zip，另有 maoqiu-v1.0.zip | Codex 首次入库 |
| [20260903](https://github.com/caixibei/agent_settings/tree/20260903) | claude / codex 双工具 v26.9.3，zip + 完整解包（1141 个文件） | 双工具同步版本号，zip 与解包并存 |
| [20260904](https://github.com/caixibei/agent_settings/tree/20260904) | codex v26.9.4 解包入库，含 pets、pet-runs | AGENTS.md + config.toml 体系入库 |
| [20260907](https://github.com/caixibei/agent_settings/tree/20260907) ～ [20260910](https://github.com/caixibei/agent_settings/tree/20260910) | codex 每日一包（v26.9.7 → v26.9.10） | 进入日更节奏 |
| [20260911](https://github.com/caixibei/agent_settings/tree/20260911) | zcode 3 个 zip，codex 同日 5 个小版本 v26.9.11.1～5 | ZCode 首次入库，单日多版本 |
| [20260912](https://github.com/caixibei/agent_settings/tree/20260912) ～ [20260914](https://github.com/caixibei/agent_settings/tree/20260914) | codex 每日一包（v26.9.12.1 → v26.9.14.1） | — |
| [20260915](https://github.com/caixibei/agent_settings/tree/20260915) | codex v26.9.15.1～2，zcode v26.9.15.1～2 | ZCode 时隔 4 天再次入库，与 codex 同步迭代 |
| [20260916](https://github.com/caixibei/agent_settings/tree/20260916) | codex v26.9.16.1～2，zcode v26.9.16.1 | codex 单日双版本迭代，zcode 同日跟进 |
| [20260917](https://github.com/caixibei/agent_settings/tree/20260917) | codex v26.9.17.1～2，zcode v26.9.17.1～2 | zcode 追加 .2 版，与 codex 同步双迭代 |
| [20260918](https://github.com/caixibei/agent_settings/tree/20260918) | codex v26.9.18.1～2，zcode v26.9.18.1～2 | zcode 追加 .2 版，与 codex 同步双迭代 |
| [20260919](https://github.com/caixibei/agent_settings/tree/20260919) | codex v26.9.19.1，zcode v26.9.19.1 | 双工具单包日更 |
| [20260920](https://github.com/caixibei/agent_settings/tree/20260920) | codex v26.9.20.1 | 当前最新 |

## 分支怎么组织

- `main` 只放仓库级公共文件：README、.gitignore、[CC使用技巧.md](CC使用技巧.md)。
- 每个日期分支 = 前一个日期分支 + 当日新增，链式递增。越新的分支内容越全，[最新分支](https://github.com/caixibei/agent_settings/tree/20260920)就是整个仓库的完整镜像。
- 提交信息统一为「备份 YYYYMMDD ：内容摘要」，提交日期与分支日期一致，`git log` 可直接按时间读。
- 每个日期分支都打有 `v` + 日期的 tag 并发布了 [GitHub Release](https://github.com/caixibei/agent_settings/releases)（如 [v20260916](https://github.com/caixibei/agent_settings/releases/tag/v20260916)），正文包含当日快照清单、迭代要点、当日提交与和上一版本的对比命令。

## 常用操作

```bash
# 看某一天的全量配置
git checkout 20260914

# 对比两个日期之间改了什么
git diff 20260913..20260914 --stat

# 只看规则目录的变化
git diff 20260806..20260810 --stat -- 20260806/rules

# 追踪某个文件的完整演变
git log --oneline 20260720..20260915 --follow -- 20260720/CLAUDE.md
```

## 目录说明

- 每个分支根目录下的日期文件夹（如 `20260914/`）就是当日快照本体。
- 大版本同时保留 zip 原包和解包目录：zip 保原始档案，解包目录方便直接阅读。
- 各分支累计约 1.4 GB，主要体积在 codex 的版本 zip 包上。
