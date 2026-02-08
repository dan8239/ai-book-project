# AI Book Project

## MANDATORY: Log Every Substantive Exchange

After EVERY substantive creative exchange (worldbuilding decisions, name choices, plot points, character details), immediately log it:

```bash
./scripts/log-interaction.sh "brief prompt summary" "brief response summary"
```

Do this BEFORE moving to the next topic. Non-substantive exchanges (clarifying questions, file reads) don't need logging.

## Project Structure

```
ai-book-project/
├── book/                   # Obsidian vault
│   ├── manuscript/         # Chapter prose
│   │   └── [act.chapter.name]/
│   │       ├── chapter.md  # Scene breakdowns → prose
│   │       └── notes.json  # Chapter metadata
│   ├── worldbuilding/      # Reference material
│   │   ├── characters/
│   │   ├── timeline/
│   │   ├── simulation/
│   │   ├── mystery/
│   │   ├── themes/
│   │   └── world/
│   └── _index.md           # Navigation hub
├── outline/
│   └── outline.xlsx        # Master outline (v_2 tab)
├── scripts/
└── references/
```

## Creative Workflow

- User speaks in canon—what they say IS the story
- Claude documents, organizes, and supports
- Don't invent names, plot points, or creative details unless explicitly asked
- When brainstorming is requested, offer options rather than decisions

## Workflow

### Obsidian Vault
- Open `book/` folder in Obsidian
- `manuscript/` for prose, `worldbuilding/` for reference
- Use wiki-links to connect concepts
- `_index.md` is the navigation hub

### Outline
- Master outline: `outline/outline.xlsx` (v_2 tab)
- Contains chapter-by-chapter breakdown with beats, purposes, and plot points

### Manuscript
- Write prose in `book/manuscript/` as markdown
- Wiki-link to `[[worldbuilding/characters/protagonist|Sam]]` etc.
- Export to Google Docs for beta readers/track changes

## Key Files

| File | Purpose |
|------|---------|
| `book/_index.md` | Navigation hub |
| `book/worldbuilding/characters/protagonist.md` | Main character arc + beats |
| `book/worldbuilding/characters/wife.md` | Wife arc (flat arc, thematic heart) |
| `outline/outline.xlsx` | Chapter-by-chapter breakdown (v_2 tab) |

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
