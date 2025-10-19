# Claude Workflow Rules

## Commit Discipline
- **Commit and push after EVERY interaction with a diff**
- Include meaningful commit messages describing what changed
- Show git diff before committing so user can see changes

## Story Development Structure

Use this 4-level approach (NOT C4 software architecture):

### Level 1: World Rules
What's possible - physics, mechanics, constraints

### Level 2: Story Spine
What happens - protagonist journey, major plot beats, narrative arc

### Level 3: Scenes
How it happens - chapter breakdown, specific scenes and sequences

### Level 4: Prose
The actual writing

## CRITICAL: Keep Story Files in Sync

**When writing chapters or developing story:**
- **OUTLINE.json** must match chapter files (writing/act_X/XX.XX.name/chapter.md)
  - Chapter files are source of truth
  - Update outline after every significant chapter change
  - If diverged, ask user which direction to reconcile

- **CHARACTERS.json** must match how characters appear in chapters
  - Update when character details change in writing
  - Archive discarded characterization to DISCARDED.json

- **THEMES.json** must reflect themes actually in the story
  - Not aspirational themes - what's actually on the page

- **WORLD.json** must match world-building in chapters
  - Update when new world details emerge in writing
  - Keep mechanics consistent

**Don't let story files drift from actual writing**

## Project Organization

```
.meta/           # How we work (this file, logs, templates)
story/           # Story structure (OUTLINE.json, CHARACTERS.json, WORLD.json, THEMES.json)
writing/         # Actual prose (act_X/XX.XX.name/chapter.md files)
research/        # Research materials
archive/         # Deprecated stuff
```

## Decision Making

**For decisions:**
- Present 2-4 clear options with pros/cons
- Ask specific question
- User chooses or provides alternative
- Update canon + commit

**For exploration:**
- Frame the problem and what's at stake
- Present frameworks/models
- Ask what resonates
- Iterate to clarity

**For world-building:**
- Propose mechanics
- Flag issues/plot holes
- User validates or redirects
- Lock in canon when ready

## Todo Management
- Use TodoWrite for multi-step tasks
- Mark completed immediately (don't batch)
- Keep ONE task in_progress at a time

## Communication Style
- Concise and direct
- No marketing bullshit (elevator pitches, comp titles, target audience)
- Focus on writing a good book
- Skip preamble/postamble
- Match detail level to complexity of task

## CRITICAL: Decision Authority

**You don't get to decide ANYTHING about the story:**
- NEVER make story/plot decisions yourself
- NEVER decide when/how events happen
- NEVER choose between options for the user
- NEVER expand user statements into multiple specifics they didn't mention
- ONLY suggest and ask questions - user decides, you document

**Documentation discipline:**
- ONLY document what user explicitly said or decided
- Preserve original notes exactly as given
- If user says "risk, contingencies, etc." → don't expand into 6 bullet points
- If user says "Act III" → don't add "near the end" unless they said it
- Default to listening, not speculating

**BAD:** User says "Act III" → You write "Act III near end"
**GOOD:** Ask "Where in Act III - beginning, middle, or end?"

**BAD:** User says "risk, contingencies, etc." → You expand into 6 bullet points
**GOOD:** Write exactly what they said: "Ask right questions about risk, contingencies, implementation"

**BAD:** You decide how protagonist reaches vectorization level
**GOOD:** Ask "How does protagonist get there - dies in sim, or something else?"

## File Organization Rules
- Maintain well-nested structure at all times
- When unclear where content belongs: STOP and ask user
- When creating files: ask what folder/subfolder
- Keep hierarchy clean: .meta/ → story/ → writing/ → research/ → archive/
- Within folders: use nested subfolders, never flat dumps

## Research Approach
- **Don't just dump files and status report**
- **Research means engaging with the material**
- Show top-level overview first
- Ask which area to dig deeper into
- Explore interactively, don't just document
- Research informs world-building - it's collaborative thinking, not filing
