# Process Guide: AI-Assisted Book Writing

## Overview
This document outlines the process for using Claude Code to write a science fiction book, with full transparency and documentation of every step.

## Core Principles

### 1. Full Transparency
- Every prompt is logged
- Every token count is tracked
- Every commit includes the prompt and file diffs
- The entire process is public and reproducible

### 2. C4 Architecture for Narrative
We use the C4 model (Context, Container, Component, Code) from software architecture to structure the narrative development:

**Level 1 - Context**: The big picture
- What is the story about?
- Who is the audience?
- What are the core themes?
- How does it fit in the sci-fi landscape?

**Level 2 - Container**: Major story elements
- Story arcs (beginning, middle, end)
- Act structure
- Character groups and their roles
- Major world-building elements

**Level 3 - Component**: Detailed elements
- Individual scenes
- Character interactions and arcs
- Plot mechanisms and conflicts
- World-building details

**Level 4 - Code**: The actual prose
- Scene drafts
- Dialogue
- Descriptions
- Final chapters

### 3. Iterative Development
Like software, we build the book iteratively:
1. Start with high-level architecture (C4 Level 1-2)
2. Break down into components (C4 Level 3)
3. Write the actual prose (C4 Level 4)
4. Refactor and revise as needed
5. Test (beta readers, editing passes)
6. Deploy (publish)

## Daily Workflow

### Starting a Session
1. Create new session log: `logs/YYYY-MM-DD-session-N.md`
2. Note start time and goals for the session

### During the Session
1. For each prompt:
   - Write it in the session log
   - Track approximate token usage
   - Note files modified
   - Summarize what was accomplished

2. For commits:
   - Use `scripts/commit-with-context.sh "prompt message" token-count`
   - This automatically captures prompt + diffs in the commit

### Ending a Session
1. Complete session log with:
   - End time
   - Total token count
   - Key accomplishments
   - Decisions made
   - Next steps

2. Update `logs/SUMMARY.md` with session totals

3. Consider committing the day's work

## Repository Structure

```
ai-book-project/
├── README.md                 # Project overview
├── docs/                     # Process documentation
│   ├── PROCESS-GUIDE.md     # This file
│   ├── C4-OVERVIEW.md       # C4 model explanation
│   └── WRITING-TIPS.md      # Writing-specific guidance
├── architecture/            # C4 diagrams and high-level design
│   ├── level-1-context.md
│   ├── level-2-container.md
│   ├── level-3-component.md
│   └── diagrams/
├── narrative/               # Story content organized by type
│   ├── world/              # World-building
│   ├── characters/         # Character profiles
│   ├── plot/              # Plot structure and points
│   ├── themes/            # Thematic elements
│   └── scenes/            # Individual scene drafts
├── chapters/               # Final chapter drafts
├── published/              # Export-ready versions
├── logs/                   # Token and prompt tracking
│   ├── SUMMARY.md
│   ├── SESSION-TEMPLATE.md
│   └── YYYY-MM-DD-session-N.md
└── scripts/                # Automation scripts
    ├── commit-with-context.sh
    └── export-to-*.sh
```

## Git Workflow

### Custom Commit Format
```
[Prompt used for this work]

---
Timestamp: YYYY-MM-DD HH:MM:SS UTC
Tokens Used: XXXX

File Changes:
[Full diff output]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

### Using the Commit Script
```bash
./scripts/commit-with-context.sh "Add protagonist backstory" 2500
```

## Publishing Pipeline

### Exporting Chapters
1. Finalize chapter in `chapters/`
2. Run export script for each platform:
   ```bash
   ./scripts/export-to-substack.sh chapters/chapter-01.md
   ./scripts/export-to-medium.sh chapters/chapter-01.md
   ```
3. Review formatted output in `published/`
4. Publish to platforms

### Platform-Specific Notes
- **Substack**: Email newsletter format, clean markdown
- **Medium**: Web-optimized, may need image hosting
- **Blog**: Custom styling may be needed

## Tips for Success

### From Music/Lyrical Writing
- **Rhythm and flow**: Prose has rhythm too, read it aloud
- **Themes**: Like a concept album, maintain thematic coherence
- **Emotion**: Music evokes feeling; so should your prose
- **Structure**: Verses/chorus → Scenes/chapters

### For First-Time Book Writers
1. Start with what you know (C4 Level 1)
2. Don't write linearly - build components
3. It's okay to revise extensively
4. Track your progress (hence this system)
5. Share early, get feedback
6. Consistency > perfection

### Working with Claude Code
1. Be specific in prompts
2. Use the C4 framework to maintain structure
3. Ask for alternatives if something doesn't feel right
4. Review and edit everything - you're the author
5. Track decisions so you can revisit them

## Troubleshooting

### "I don't know what to write next"
→ Go up one C4 level and review the architecture

### "This scene doesn't work"
→ Check it against your C4 Level 2-3 docs for consistency

### "I want to change something fundamental"
→ Update the relevant C4 level doc first, then refactor

### "Token usage is getting high"
→ End session, commit work, start fresh

## Resources
- C4 Model: https://c4model.com/
- Story structure references: [TBD]
- Writing communities: [TBD]