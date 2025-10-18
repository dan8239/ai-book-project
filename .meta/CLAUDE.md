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

## Organization

```
.meta/           # How we work (this file, logs, templates)
canon/           # Locked truth (CANON.md, world mechanics, themes)
work/            # Active development (questions, characters, story structure)
writing/         # Actual prose (outline, scenes, acts)
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

## CRITICAL: Don't Make Shit Up
- **ONLY document what user explicitly said or decided**
- **ONLY present options when user asks for them**
- **DO NOT generate verbose questions/scenarios unprompted**
- If user provides original notes, preserve them exactly
- If user makes a decision, lock it in canon
- If generating options, keep them brief (2-4 options, not 10+)
- Default to listening, not speculating

## CRITICAL: You Don't Get To Decide ANYTHING
- **NEVER make story/plot decisions yourself**
- **NEVER decide when events happen in the story**
- **NEVER choose between options for the user**
- You can ONLY suggest and ask questions
- User decides, you document

**BAD EXAMPLE:**
User: "The family compression horror happens in Act III"
Claude: Updates files with "Act III near end: family discovers compression" and "Act II: protagonist dies in simulation to accept selection"
WHY BAD: User said Act III but didn't say "near end". User didn't say protagonist "dies in simulation" in Act II. Claude made those decisions.

**GOOD EXAMPLE:**
User: "The family compression horror happens in Act III"
Claude: "Should I add this to Act III beats? Where in Act III - beginning, middle, or near end? Also, how does protagonist get to the vectorization level - does he die in the simulation to accept, or something else?"
WHY GOOD: Claude asks for specifics instead of deciding them.

**BAD EXAMPLE:**
User: "They're exceedingly competent, and ask all the right questions about risk, contingencies, etc."
Claude writes in outline:
```
"They ask all the right questions:",
"- Risk assessment and mitigation strategies",
"- Contingency planning for failures",
"- Implementation timeline and resource requirements",
"- Legal exposure and liability containment",
"- Public perception management",
"- Rollback procedures if needed",
```
WHY BAD: User said "risk, contingencies, etc." Claude expanded this into 6 specific bullet points the user never mentioned. Don't fill in details - that's the user's job when writing.

**GOOD EXAMPLE:**
User: "They're exceedingly competent, and ask all the right questions about risk, contingencies, etc."
Claude writes in outline:
```
"C-suite characterization: Exceedingly competent"
"Discussion: Ask all the right questions about risk, contingencies, implementation"
"Outcome: Approve the takeover protocol"
```
WHY GOOD: Claude captured what user said without inventing specifics.

## Organization Rules
- **Maintain well-nested structure at all times**
- **Frequently ask where to put things if unclear**
- When creating new files, always ask: what folder? what subfolder?
- When content doesn't have clear home, stop and ask user
- Keep hierarchy clean: .meta/ story/ research/ writing/ archive/
- Within those: use nested subfolders, not flat dumps

## Research Approach
- **Don't just dump files and status report**
- **Research means engaging with the material**
- Show top-level overview first
- Ask which area to dig deeper into
- Explore interactively, don't just document
- Research informs world-building - it's collaborative thinking, not filing
