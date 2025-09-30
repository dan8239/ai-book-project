# Questions & Decisions Tracker

## Format
Each question gets:
- **ID**: Q### for tracking
- **Status**: OPEN / DECIDED / BLOCKED (waiting on other decision)
- **Category**: Plot / Character / World / Structure / Theme / Technical
- **Priority**: P0 (blocks progress) / P1 (important) / P2 (nice to have)
- **Decision**: Final answer when resolved
- **Rationale**: Why we chose this

---

## Open Questions

### P0 - Blocks Progress

**Q001** - What is the actual loss function being optimized?
- **Category**: Plot, Theme
- **Context**: The entire simulation exists to optimize something. Options mentioned: energy capture, DNA survival, interstellar travel, or something else. This shapes the entire thematic core.
- **Dependencies**: Affects character motivations, world rules, ending
- **Status**: OPEN

**Q002** - When/how does the reader learn they're in a simulation?
- **Category**: Structure
- **Context**: Early reveal changes the reading experience entirely vs. late twist. Affects whether we're writing mystery or philosophical exploration.
- **Options**:
  - A) Obvious from chapter 1 (reader knows, protagonist doesn't)
  - B) Gradual reveals throughout (reader and protagonist discover together)
  - C) Final act twist (both shocked)
- **Status**: OPEN

**Q003** - Is the protagonist a single person or multiple instances?
- **Category**: Character, Structure
- **Context**: Notes mention "Run Lola Run" parallel tracks and "dual track" home/work life. Are these literally different simulation instances of the same person?
- **Impact**: Changes POV structure, narrative complexity, thematic weight
- **Status**: OPEN

### P1 - Important But Not Blocking

**Q004** - What exactly does the devsecops message contain?
- **Category**: Plot
- **Context**: He spends 21 years planting backdoors to hide a message. What is it? Proof of simulation? Escape instructions? Just a warning?
- **Dependencies**: Q002 (reveal timing)
- **Status**: OPEN

**Q005** - What happens to selected individuals after "passing"?
- **Category**: Plot, World
- **Context**: Notes say they "exit the main loop" and help "decide the adjustment to the loss function." But is this real or another layer of simulation?
- **Options**:
  - A) Actually become part of the optimizer system
  - B) It's another simulation layer (turtles all the way down)
  - C) Intentionally ambiguous
- **Status**: OPEN

**Q006** - How much of the science should be real vs. extrapolated?
- **Category**: Technical, Style
- **Context**: You want "cutting edge ML + a smidge" and mentioned quantum computing. Need to establish boundaries for handwaving vs. hard science.
- **Status**: OPEN

**Q007** - Tone calibration: How dark vs. funny?
- **Category**: Style
- **Context**: You want Claude assistant to be hilarious and swear, but the premise is existentially bleak. What's the balance?
- **Status**: OPEN

### P2 - Nice to Have / Can Decide Later

**Q008** - Timestamp format and reveal mechanism?
- **Category**: Style
- **Context**: Notes say start with ambiguous "0.217.293.294" then reveal it's milliseconds. When does this click for the reader?
- **Status**: OPEN

**Q009** - How many character POVs?
- **Category**: Structure
- **Context**: Devsecops guy, protagonist data scientist, others?
- **Dependencies**: Q003
- **Status**: OPEN

**Q010** - Sports as test suites - keep this metaphor?
- **Category**: World, Theme
- **Context**: Interesting idea but could be distracting. Does it serve the core story?
- **Status**: OPEN

---

## Decided Questions
_(None yet - will populate as we make decisions)_

---

## User's Original Questions (From Notes)

### From "Questions to answer" section:
- What are they studying
- Why is a simulation needed
- Why is it a genetic algorithm that's best suited to the problem
- What is the loss function that led to us optimizing like this?
- Who's at the top of the pyramid running it all?
- Why does it need to be recursive or repeating?
- How does the simulation realism/granularity change?
- How do generations and epochs work?
- How does selection work?
- How did we get here?
- How did all the data get captured
- Limiting factor of memory
- How many people's brains and circumstances could be copied?

**Note**: Many of these are narrative questions (what the characters discover) vs. author questions (what we need to decide). Need to separate which are mysteries to preserve vs. mechanics we must define.