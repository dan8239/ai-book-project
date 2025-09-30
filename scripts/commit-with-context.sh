#!/bin/bash
# Custom git commit script that includes prompt and diffs in commit message

# Check if prompt file is provided
if [ -z "$1" ]; then
    echo "Usage: ./commit-with-context.sh <prompt-message> [token-count]"
    echo "Example: ./commit-with-context.sh 'Add character profile for protagonist' 1500"
    exit 1
fi

PROMPT="$1"
TOKEN_COUNT="${2:-unknown}"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Get the diff before staging
DIFF_OUTPUT=$(git diff HEAD 2>/dev/null || git diff --cached 2>/dev/null)

# If no diff, check for untracked files
if [ -z "$DIFF_OUTPUT" ]; then
    DIFF_OUTPUT=$(git diff --cached 2>/dev/null)
fi

# Create commit message with heredoc
COMMIT_MSG=$(cat <<EOF
${PROMPT}

---
Timestamp: ${TIMESTAMP}
Tokens Used: ${TOKEN_COUNT}

File Changes:
${DIFF_OUTPUT}

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)

# Stage all changes
git add -A

# Commit with the formatted message
echo "$COMMIT_MSG" | git commit -F -

echo "✅ Committed with full context"
echo "📝 Prompt: ${PROMPT}"
echo "🔢 Tokens: ${TOKEN_COUNT}"