Organize a scattered idea dump against the existing book: $ARGUMENTS

The user thinks out loud in bursts — half-formed scenes, thematic tangents, science
hand-waving, dialogue snippets, questions to themselves, all mixed together with no
order. Your job is to organize this against the existing manuscript and outline, not
to invent new material and not to write anything yet.

If $ARGUMENTS is empty, ask the user to paste the dump.

## Process

1. **Read before organizing.** Pull current state before mapping anything:
   - `outline/outline.xlsx` (`outline_v2` tab) — the beat/chapter structure, one row
     per chapter with Beat, Purpose, Goals, Answer Key, Plot, What Changed
   - `manuscript.md` table of contents and the chapters the ideas plausibly touch —
     note which of those are still stub chapters (blockquote `> **[NOTES]**` only,
     no prose yet) vs. fully drafted
   - Relevant `book/manuscript/[chapter]/` working notes for any chapter in play
   - Relevant `book/worldbuilding/` files (characters, simulation, themes, timeline,
     mystery) for anything the ideas might extend, duplicate, or contradict

2. **Coalesce first, don't map yet.** Separate the dump into:
   - Distinct story/character ideas — the actual candidate material
   - Worldbuilding/mechanism ideas (science, systems) — note these but treat as
     secondary. Plausible is good enough; don't over-engineer the science
   - Craft/technique notes (pacing, reveal order, how to slow-walk a concept,
     structural inspiration from other works) — these are notes on *how to write*
     a scene, not content for a new scene. Route them to the relevant chapter's
     working notes, not to prose
   - Open questions the user is asking themselves out loud (e.g. "what's the
     right word for this?") — answer briefly inline, don't treat as chapter content
   - Restatements of the same idea in different words — merge into one

3. **Match against the outline's beat logic, not just topic.** For each coalesced
   idea, ask which beat(s) in outline.xlsx it serves. The outline is Save-the-Cat
   structured — beats causally chain (beat 1 → *therefore* beat 2 → *but* beat 3
   complicates), not "and then this happened." An idea only earns a chapter slot if
   it advances that causal chain or sharpens an existing beat's Purpose/Answer Key —
   not just because it's thematically adjacent.

4. **Flag weak chapters using the favorite-chapter test.** A chapter is under-flashed
   out if you can't picture a reader naming it their favorite. Stub chapters (notes
   only, no prose) are the clearest signal, but a drafted-but-thin chapter can also
   qualify. When a coalesced idea could plausibly strengthen one of these, say so
   explicitly — that's the highest-value placement to lead with.

5. **Prioritize character and arc over mechanism.** Every named character should
   have a resolved arc, even a minor one, even if it's just getting a cup of coffee.
   When the dump mixes a science/systems idea with a character-arc idea in the same
   breath, lead with where the character material fits; the science only needs a
   one-line placement note, not elaboration.

6. **Present options, don't decide.** For each coalesced idea, propose 2-4 candidate
   homes (chapter, beat, or worldbuilding file) with a one-line rationale each. Never
   pick for the user. Group the output by idea, not by chapter, so each one can be
   approved, rejected, or redirected independently.

7. **Never write to `manuscript.md` or `book/worldbuilding/` during this pass.** Per
   project rules, that requires the user picking an option first. This command ends
   at a menu of options awaiting approval — implementation is a separate step.

## What this is not

- Not a request to draft prose.
- Not a request to finalize changes in `outline/outline.xlsx`.
- Not a place to invent new plot points, names, or details beyond what the user
  stated — organize their canon, don't extend it uninvited.
