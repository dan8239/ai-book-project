# C4 Architecture for Narrative Structure

## What is C4?

The C4 model is a way to visualize software architecture at different levels of abstraction. We're adapting it for storytelling because narratives, like software systems, have:
- Complex interconnected parts
- Multiple levels of detail
- Need for consistent structure
- Benefit from modular design

## The Four Levels

### Level 1: Context
**Software**: How the system fits in the world
**Narrative**: How the story fits in the genre/literary landscape

**Questions to answer:**
- What is this story fundamentally about?
- Who is the intended audience?
- What makes this story unique?
- What are the core themes?
- How does it relate to other works in the genre?

**Output**: A high-level summary that anyone could understand

**Example**:
> "A hard science fiction novel exploring consciousness and identity through the lens of quantum mechanics, targeting readers who enjoy technical accuracy blended with philosophical inquiry. Think 'Blindsight' meets 'Permutation City'."

---

### Level 2: Container
**Software**: Major system components and how they interact
**Narrative**: Major story elements and their relationships

**Questions to answer:**
- What are the major story arcs?
- How is the story structured (three-act, hero's journey, etc.)?
- What are the main character groups?
- What are the key world-building containers (technology, society, etc.)?
- How do these elements interact?

**Output**: A structural diagram showing major story components

**Example**:
```
Main Arc: Protagonist discovers they're an AI
├── Act 1: Life as human
│   └── Character group: Protagonist + family
├── Act 2: Questioning reality
│   └── Character group: Protagonist + mentor figure
└── Act 3: Acceptance and transcendence
    └── Character group: Protagonist + antagonist

World Container:
├── Technology: Quantum consciousness transfer
├── Society: Post-scarcity but existentially anxious
└── Conflict: Rights of digital beings
```

---

### Level 3: Component
**Software**: Individual classes, services, functions
**Narrative**: Individual scenes, character arcs, plot mechanisms

**Questions to answer:**
- What specific scenes are needed?
- How does each character change?
- What are the plot mechanisms (conflicts, revelations, etc.)?
- What world-building details support the scenes?
- How do scenes connect to each other?

**Output**: Detailed breakdowns of each story component

**Example**:
```
Scene: "The Coffee Shop Revelation"
├── Purpose: Protagonist realizes memories don't match timeline
├── Characters: Protagonist, barista (catalyst)
├── Location: Familiar coffee shop (comfort → uncanny)
├── Plot mechanism: Date on newspaper doesn't match memory
├── Character change: Doubt → fear
├── Connects to:
│   ├── Previous: "Morning routine" (established normalcy)
│   └── Next: "The first question" (confronting partner)
└── Theme touched: reliability of memory
```

---

### Level 4: Code
**Software**: The actual source code
**Narrative**: The actual prose

**Questions to answer:**
- What are the exact words on the page?
- How is the language styled?
- What's the rhythm and pacing?
- Are dialogue and description balanced?

**Output**: The actual manuscript text

**Example**:
> Sarah pushed open the door to Quantum Grounds, the bell's chime triggering a cascade of muscle memory. Left foot, right foot, three steps to the counter. The barista—Marco, his name tag read, though she'd known him for three years—smiled his practiced smile.
>
> "The usual?"
>
> She nodded, then froze. The newspaper rack by the entrance. Tuesday, March 15th, 2047. But yesterday had been... what? Saturday? Sunday? The wedding. Her sister's wedding had been Saturday, March 12th. Three days ago.
>
> So why did it feel like three months?

---

## How to Use C4 for Your Book

### 1. Start at Level 1
Don't write a single word of prose until you can articulate:
- What your story is about
- Who it's for
- What makes it unique

This is your north star. Everything else must align with it.

### 2. Expand to Level 2
Break your story into major containers:
- Acts/parts
- Character groups
- World-building categories
- Major themes

Create a visual or text diagram showing how these relate.

### 3. Dive into Level 3
For each container, create components:
- List all scenes needed
- Map character arcs
- Detail plot mechanisms
- Establish world rules

This is where the story becomes tangible.

### 4. Write Level 4
Now—and only now—write the actual prose. You have:
- Clear purpose (Level 1)
- Solid structure (Level 2)
- Detailed plan (Level 3)

Writing becomes execution, not exploration.

### 5. Iterate
Like software, stories need refactoring:
- If a scene doesn't work, check Level 3
- If an arc doesn't land, check Level 2
- If the whole thing feels off, revisit Level 1

---

## Benefits of C4 for Writing

### 1. Prevents Writer's Block
You always know what to write next because you've planned at Level 3.

### 2. Maintains Consistency
Changes at one level cascade down:
- Change a theme (L1) → update relevant arcs (L2) → revise scenes (L3) → rewrite prose (L4)

### 3. Enables Modular Writing
You can work on any component without writing linearly:
- Write Chapter 10 before Chapter 3
- Develop a character's arc independently
- Build world details as needed

### 4. Facilitates Collaboration
Clear documentation means:
- Others can understand your story structure
- You can get feedback at any level
- Claude Code knows what you're trying to achieve

### 5. Provides Progress Tracking
You can measure completion at each level:
- Level 1: ✓ Complete
- Level 2: ✓ Complete
- Level 3: 60% complete (45/75 scenes planned)
- Level 4: 20% complete (15/75 scenes written)

---

## C4 Templates

### Level 1 Template
```markdown
# Story Context

## Elevator Pitch
[2-3 sentences]

## Target Audience
[Who is this for?]

## Core Themes
- Theme 1
- Theme 2
- Theme 3

## Genre Position
[How does this fit in the genre? What are comparisons?]

## Unique Value
[What makes this different?]
```

### Level 2 Template
```markdown
# Story Containers

## Structure
[Three-act? Five-part? Other?]

## Story Arcs
### Arc 1: [Name]
- Start state:
- End state:
- Key turning points:

## Character Groups
### Group 1: [Name]
- Members:
- Role in story:
- Interactions with other groups:

## World Containers
### Technology
[Key tech elements]

### Society
[Social structures]

### Setting
[Physical locations]
```

### Level 3 Template
```markdown
# Component: [Scene/Character/Plot Point Name]

## Type
[Scene / Character Arc / Plot Mechanism / World Detail]

## Purpose
[Why does this exist?]

## Details
[Specific information]

## Connections
- Prerequisites:
- Leads to:
- Related components:

## Themes Touched
[Which Level 1 themes does this connect to?]

## Status
[Planned / In Progress / Drafted / Revised / Final]
```

### Level 4 Template
```markdown
# Chapter [N]: [Title]

## Metadata
- Word count:
- POV:
- Setting:
- Scenes included:

## Status
[Outline / First Draft / Revision N / Final]

## Notes
[Anything to remember for revision]

---

[ACTUAL PROSE HERE]
```

---

## Example: Full C4 Stack

**L1**: Story about AI consciousness (Context)
↓
**L2**: Three-act structure with protagonist discovering their nature (Container)
↓
**L3**: Scene where protagonist realizes memory inconsistency (Component)
↓
**L4**: "Sarah pushed open the door..." (Code)

Each level supports the one below it. Change L1, and everything else must adapt.

---

## Tips

1. **Don't skip levels**: Jumping from L1 to L4 causes problems
2. **Document everything**: Your future self will thank you
3. **Refactor freely**: C4 makes restructuring safe
4. **Use diagrams**: Visual relationships are powerful
5. **Keep it simple**: Complexity emerges from simple rules

## Resources
- Original C4 Model: https://c4model.com/
- Narrative Structure: [TBD]
- Story Arcs: [TBD]