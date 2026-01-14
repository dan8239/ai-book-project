# AI Book Project

## Project Structure

```
ai-book-project/
├── worldbuilding/          # Obsidian vault - reference material
│   ├── characters/         # Character files with arcs
│   ├── timeline/           # Era definitions
│   ├── simulation/         # Sim world details
│   ├── mystery/            # Clue paths
│   ├── themes/             # Themes, motifs, style guide
│   └── _index.md           # Navigation hub
├── manuscript/             # Chapter files (planning + prose)
│   └── [act.chapter.name]/ # Each chapter folder
│       ├── chapter.md      # Scene breakdowns, then prose
│       └── notes.json      # Chapter metadata
├── outline/                # Structure tracking
│   └── outline.csv         # Synced with Google Sheet
├── scripts/
│   └── sync-outline.sh     # Pull from Google Sheet to CSV
└── references/             # Research, inspiration
```

## Workflow

### Worldbuilding (Obsidian)
- Open `worldbuilding/` folder in Obsidian
- Use wiki-links to connect concepts
- Character arcs live in character files
- `_index.md` is the navigation hub

### Outline (Google Sheets ↔ CSV)
- Master outline lives in Google Sheet: `1N8DdsXJxRHvBXT1OhOviCNYx9wbZg1XJWgqIBlJihqc`
- Sync TO sheet: Ask Claude to sync outline.csv to Google Sheet
- Sync FROM sheet: Run `./scripts/sync-outline.sh`
- CSV is version controlled, Sheet is for editing

### Manuscript (Markdown → Export)
- Write prose in `manuscript/` as markdown
- Export to Google Docs when needing beta readers/track changes
- Keep planning/structure version controlled here

## Key Files

| File | Purpose |
|------|---------|
| `worldbuilding/_index.md` | Navigation for all worldbuilding |
| `worldbuilding/characters/protagonist.md` | Main character arc + beats |
| `worldbuilding/characters/wife.md` | Wife arc (flat arc, thematic heart) |
| `outline/outline.csv` | Chapter-by-chapter breakdown |

## Logging

All interactions are logged to `logs/interactions.db` (SQLite).

### Scripts
- `scripts/log-interaction.sh "prompt" "response"` — log a single interaction
- `scripts/session-commit.sh "summary"` — commit all changes with interaction count

### Workflow
1. At end of each substantive interaction, log it
2. At end of session, run `./scripts/session-commit.sh "Session summary"`

### Querying logs
```bash
# View today's interactions
sqlite3 logs/interactions.db "SELECT * FROM interactions WHERE session_date = date('now');"

# Count by day
sqlite3 logs/interactions.db "SELECT session_date, COUNT(*) FROM interactions GROUP BY session_date;"
```
