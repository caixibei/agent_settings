#!/usr/bin/env node
/**
 * PreToolUse hook（用户级通用）：环境配置文件（application*.yml）编辑前升级为用户确认。
 *
 * 业务背景：各项目的 application*.yml 通常包含真实数据源等敏感配置，敏感配置
 * 修改前应由用户确认。本 hook 把该约定硬化为机制：命中目标文件名时返回
 * permissionDecision=ask，由 Claude Code 弹出确认框交用户裁决；未命中时静默
 * 放行，不给普通编辑增加确认负担。
 */
const fs = require('fs');

// stdin 读取：解析失败视为无有效输入，直接放行走正常权限流程
let raw = '';
try { raw = fs.readFileSync(0, 'utf8'); } catch (e) { process.exit(0); }
let payload = null;
try { payload = JSON.parse(raw); } catch (e) { process.exit(0); }

const filePath = (payload && payload.tool_input && payload.tool_input.file_path) || '';
const fileName = filePath.replace(/\\/g, '/').split('/').pop() || '';

// 仅按文件名匹配环境配置文件；其余文件不输出且退出码 0，不改变原有权限行为
if (/^application.*\.ya?ml$/i.test(fileName)) {
  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'ask',
      permissionDecisionReason: '该文件为环境配置文件，可能含数据源等敏感配置，修改前需用户确认。',
    },
  }));
}
process.exit(0);
