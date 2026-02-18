# AI Book Project

## MANDATORY: Log Every Substantive Exchange

After EVERY substantive creative exchange (worldbuilding decisions, name choices, plot points, character details), immediately log it:

```bash
./scripts/log-interaction.sh "brief prompt summary" "brief response summary"
```

Do this BEFORE moving to the next topic. Non-substantive exchanges (clarifying questions, file reads) don't need logging.

## Source of Truth

**`manuscript.md`** — The book. One file, tracked by git. This is the only diff that matters.

- Prose is regular text
- Unwritten chapters have notes in blockquotes (`>`)
- `git log -p manuscript.md` shows the book's evolution over time

### Exporting

```bash
./scripts/export-manuscript.sh docx   # For sharing with beta readers
./scripts/export-manuscript.sh epub   # For e-readers
./scripts/export-manuscript.sh pdf    # For print preview
```

The export script strips blockquoted notes and converts via pandoc.

## Project Structure

```
ai-book-project/
├── manuscript.md           # THE BOOK — source of truth, git-tracked
├── manuscript.docx         # Generated export (gitignored)
├── book/                   # Obsidian vault
│   ├── manuscript/         # Chapter working notes & drafts
│   │   └── [act.chapter.name]/
│   │       ├── chapter.md  # Scene breakdowns, drafts
│   │       └── notes.md    # Chapter research & planning
│   ├── worldbuilding/      # Reference material
│   │   ├── characters/
│   │   ├── timeline/
│   │   ├── simulation/
│   │   ├── mystery/
│   │   ├── themes/
│   │   └── world/
│   └── _index.md           # Navigation hub
├── outline/
│   └── outline.xlsx        # Master outline (outline_v2 tab)
├── scripts/
└── references/
```

## Creative Workflow

- User speaks in canon—what they say IS the story
- Claude documents, organizes, and supports
- Don't invent names, plot points, or creative details unless explicitly asked
- When brainstorming is requested, offer options rather than decisions
- New prose goes directly into `manuscript.md`
- Working notes, research, and planning stay in `book/manuscript/` chapter folders

## Workflow

### Writing
- Edit `manuscript.md` directly — in Obsidian, VS Code, or any editor
- When ready to share: `./scripts/export-manuscript.sh docx`

### Obsidian Vault
- Open `book/` folder in Obsidian for worldbuilding reference
- Chapter folders in `book/manuscript/` hold working notes, NOT the book
- Use wiki-links to connect concepts
- `_index.md` is the navigation hub

### Outline
- Master outline: `outline/outline.xlsx` (outline_v2 tab)
- 26 chapters from Prologue through Coda, following Save the Cat beat structure
- Contains chapter-by-chapter breakdown with beats, purposes, and plot points

## Key Files

| File | Purpose |
|------|---------|
| `manuscript.md` | **THE BOOK** — single source of truth |
| `outline/outline.xlsx` | Chapter-by-chapter breakdown (outline_v2 tab) |
| `book/_index.md` | Obsidian navigation hub |
| `book/worldbuilding/characters/protagonist.md` | Main character arc + beats |
| `book/worldbuilding/characters/wife.md` | Wife arc (flat arc, thematic heart) |
| `scripts/export-manuscript.sh` | Export to docx/epub/pdf |

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
