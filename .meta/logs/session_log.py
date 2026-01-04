#!/usr/bin/env python3
"""
Session log database for AI Book Project.
Stores: date, session_id, prompt, response
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "sessions.db"

def init_db():
    """Initialize the database with schema."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            session_id TEXT NOT NULL,
            prompt TEXT NOT NULL,
            response TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('CREATE INDEX IF NOT EXISTS idx_session_id ON sessions(session_id)')
    c.execute('CREATE INDEX IF NOT EXISTS idx_date ON sessions(date)')
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

def log_prompt(session_id: str, prompt: str, response: str, date: str = None):
    """Log a prompt/response pair."""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO sessions (date, session_id, prompt, response)
        VALUES (?, ?, ?, ?)
    ''', (date, session_id, prompt, response))
    conn.commit()
    row_id = c.lastrowid
    conn.close()
    return row_id

def get_session(session_id: str):
    """Get all prompts for a session."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM sessions WHERE session_id = ? ORDER BY id', (session_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_recent(n: int = 10):
    """Get n most recent prompts."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM sessions ORDER BY id DESC LIMIT ?', (n,))
    rows = c.fetchall()
    conn.close()
    return rows

def export_json(output_path: str = None):
    """Export all sessions to JSON."""
    if output_path is None:
        output_path = DB_PATH.parent / "sessions_export.json"

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM sessions ORDER BY id')
    rows = c.fetchall()
    conn.close()

    data = [
        {
            "id": r[0],
            "date": r[1],
            "session_id": r[2],
            "prompt": r[3],
            "response": r[4],
            "created_at": r[5]
        }
        for r in rows
    ]

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Exported {len(data)} entries to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "init":
            init_db()
        elif cmd == "recent":
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            for row in get_recent(n):
                print(f"[{row[1]}] {row[2]}: {row[3][:80]}...")
        elif cmd == "export":
            export_json()
        else:
            print("Usage: session_log.py [init|recent N|export]")
    else:
        print("Usage: session_log.py [init|recent N|export]")
