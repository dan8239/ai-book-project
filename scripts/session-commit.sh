#!/bin/bash
# Commit all changes at end of session with interaction count
# Usage: ./session-commit.sh "Session summary"

DB_PATH="$(dirname "$0")/../logs/interactions.db"
TODAY=$(date +"%Y-%m-%d")

# Count today's interactions
if [ -f "$DB_PATH" ]; then
    INTERACTION_COUNT=$(sqlite3 "$DB_PATH" "SELECT COUNT(*) FROM interactions WHERE session_date = '$TODAY';")
else
    INTERACTION_COUNT=0
fi

SUMMARY="${1:-Session work}"

# Stage all changes
git add -A

# Create commit message
git commit -m "$(cat <<EOF
$SUMMARY

---
Date: $TODAY
Interactions this session: $INTERACTION_COUNT

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

# Push to remote
git push

echo "Committed and pushed session: $SUMMARY ($INTERACTION_COUNT interactions)"
