# AI Book Project

## Creative Collaboration Loop

All substantive work follows this loop:

1. **Clarify** — Read relevant files, ask questions, understand intent
2. **Plan** — Present what will change, where, and why
3. **Approve** — User approves, adjusts, or rejects the plan
4. **Implement** — Only then write to files

**Never write to `manuscript.md` or `book/worldbuilding/` without explicit approval.** Research, reading, and organizing ideas in conversation is always fine — writing to files requires a green light.

## Source of Truth

**`manuscript.md`** — The book. One file, tracked by git. This is the only diff that matters.

- Prose is regular text
- Unwritten chapters have notes in blockquotes (`>`)
- `git log -p manuscript.md` shows the book's evolution over time

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
- When ready to share: `/export docx`

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
| `scripts/export-manuscript.sh` | Export to docx/epub/pdf |
| `scripts/session-commit.sh` | Commit all changes with summary |
