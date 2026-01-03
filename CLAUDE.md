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

## Story Summary

A simulation optimization expert discovers his world is one of 847 million trials. His journey from "saving the planet" to "being present with family" mirrors the discovery that the only thing he can actually save is his family - by copying their simulation to a hidden server before the epoch ends.

### Main Characters
- **Protagonist** - ML expert, arc from saving-world to saving-family
- **Wife** - Flat arc, embodies "this is the only trial we get"
- **Big Dog** - Global scope agent, functional villain
- **DevSecOps Woman** - Ancestor who planted the seed data 100 years ago
- **Coffee Guy** - Real world, ironic flat arc

### Key Themes
- The 0.3% who act
- Loss functions as ideology
- We are all snapshots in time
- Presence over achievement
