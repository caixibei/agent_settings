#!/bin/bash
# git-safety-check.sh — PreToolUse hook for Bash
# 拦截 git reset --hard / clean -fd / checkout -- 等破坏性命令，
# 防止子代理或误操作导致未提交更改永久丢失。
#
# 使用方式：在 settings.json 的 PreToolUse 中注册为 Bash matcher

COMMAND=""
[ -n "${CLAUDE_TOOL_INPUT:-}" ]          && COMMAND="$CLAUDE_TOOL_INPUT"
[ -z "$COMMAND" ] && [ -n "${1:-}" ]    && COMMAND="$1"
[ -z "$COMMAND" ] && [ ! -t 0 ]         && COMMAND=$(cat 2>/dev/null)
[ -z "$COMMAND" ] && [ -n "${CLAUDE_TOOL_ARGS:-}" ] && COMMAND="$CLAUDE_TOOL_ARGS"

# 无法读取命令内容时放行（不误杀）
[ -z "$COMMAND" ] && exit 0

# 匹配破坏性 git 模式
if echo "$COMMAND" | grep -qE '(git\s+reset\s+--hard|git\s+clean\s+-[df]|git\s+checkout\s+--)'; then
  echo "⛔ 拦截到破坏性 git 命令。该命令将永久删除未提交的更改。"
  echo ""
  echo "   未提交文件（当前目录）："
  git status --short 2>/dev/null | head -20
  echo ""
  echo "   如确认要执行，请先确保所有未提交更改已备份或提交。"
  exit 1
fi

exit 0
