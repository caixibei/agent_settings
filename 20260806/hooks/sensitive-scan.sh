#!/bin/bash
# sensitive-scan.sh - 敏感信息扫描 Hook
# 在编辑文件后自动检测硬编码的敏感信息

FILE_PATH="$1"

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
    exit 0
fi

# 只扫描代码文件
case "$FILE_PATH" in
    *.java|*.vue|*.js|*.ts|*.xml|*.yml|*.yaml|*.properties|*.json)
        ;;
    *)
        exit 0
        ;;
esac

# 敏感信息模式（排除注释、日志输出）
SENSITIVE_PATTERNS=(
    'password\s*=\s*["\x27][^"\x27]+["\x27]'
    'secret\s*=\s*["\x27][^"\x27]+["\x27]'
    'token\s*=\s*["\x27][^"\x27]+["\x27]'
    'api[_-]?key\s*=\s*["\x27][^"\x27]+["\x27]'
    'private[_-]?key\s*=\s*["\x27][^"\x27]+["\x27]'
    'jdbc:[a-z]+://[^"\x27\s]+password=[^"\x27\s]+'
    '"password"\s*:\s*"[^"]+"'
    '"secret"\s*:\s*"[^"]+"'
    '"token"\s*:\s*"[^"]+"'
    '"apiKey"\s*:\s*"[^"]+"'
    '"privateKey"\s*:\s*"[^"]+"'
)

# 排除模式（注释、日志、占位符）
EXCLUDE_PATTERNS=(
    '^\s*//'
    '^\s*\*'
    '^\s*#'
    '^\s*/\*'
    'log\.(info|debug|warn|error)'
    'System\.out\.print'
    'placeholder'
    'xxx'
    'your-'
    'example'
    '^[Tt]est[A-Z]'
    'testConfig'
)

FOUND_ISSUES=0

for pattern in "${SENSITIVE_PATTERNS[@]}"; do
    # 找到匹配行
    MATCHES=$(grep -in "$pattern" "$FILE_PATH" 2>/dev/null | head -5)

    if [ -n "$MATCHES" ]; then
        while IFS= read -r line; do
            LINE_NUM=$(echo "$line" | cut -d: -f1)
            CONTENT=$(echo "$line" | cut -d: -f2-)

            # 检查是否在排除模式中
            EXCLUDED=0
            for exclude in "${EXCLUDE_PATTERNS[@]}"; do
                if echo "$CONTENT" | grep -q "$exclude" 2>/dev/null; then
                    EXCLUDED=1
                    break
                fi
            done

            if [ $EXCLUDED -eq 0 ]; then
                echo "⚠️  检测到可能的敏感信息硬编码"
                echo "   文件: $FILE_PATH"
                echo "   行号: $LINE_NUM"
                echo "   内容: $(echo "$CONTENT" | sed 's/^[[:space:]]*//' | cut -c1-80)"
                echo ""
                FOUND_ISSUES=1
            fi
        done <<< "$MATCHES"
    fi
done

if [ $FOUND_ISSUES -eq 1 ]; then
    echo "建议：使用配置中心、环境变量或密钥管理服务存储敏感信息"
fi

exit 0
