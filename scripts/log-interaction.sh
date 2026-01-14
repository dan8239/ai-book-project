#!/bin/bash
# Log a Claude interaction to SQLite database
# Usage: ./log-interaction.sh "prompt text" "response text"

DB_PATH="$(dirname "$0")/../logs/interactions.db"

# Initialize database if it doesn't exist
if [ ! -f "$DB_PATH" ]; then
    sqlite3 "$DB_PATH" <<EOF
CREATE TABLE interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT (datetime('now')),
    session_date TEXT DEFAULT (date('now')),
    prompt TEXT NOT NULL,
    response TEXT NOT NULL
);
CREATE INDEX idx_session_date ON interactions(session_date);
EOF
    echo "Created new database at $DB_PATH"
fi

PROMPT="$1"
RESPONSE="$2"

if [ -z "$PROMPT" ] || [ -z "$RESPONSE" ]; then
    echo "Usage: ./log-interaction.sh \"prompt\" \"response\""
    exit 1
fi

# Escape single quotes for SQLite
PROMPT_ESCAPED="${PROMPT//\'/\'\'}"
RESPONSE_ESCAPED="${RESPONSE//\'/\'\'}"

sqlite3 "$DB_PATH" "INSERT INTO interactions (prompt, response) VALUES ('$PROMPT_ESCAPED', '$RESPONSE_ESCAPED');"

echo "Logged interaction at $(date)"
