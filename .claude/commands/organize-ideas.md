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

2. **Capture losslessly. Never paraphrase the user's own words.** Not a word of
   what the user wrote gets changed, cleaned up, or summarized into your own prose.
   Their exact sentences and phrasing are quoted verbatim into wherever they end up
   filed. If you have a suggestion, a question, or a proposed modification, it gets
   *appended* as a clearly labeled addition (e.g. `[Claude suggestion]` /
   `[Claude question]`) — never blended into or rewriting their text. Restatements
   of the same idea in different words are still kept, side by side, not merged
   into a single cleaned-up version — the user's repetitions and false starts are
   part of the raw material, not noise to remove. The one exception: distinguish
   plain factual questions the user is asking *you* (e.g. "what's the right word
   for this?", "what file actually stores X?") — answer those inline/briefly, they
   aren't story content.

3. **File everything under chapter/beat, nested, not under a separate notes
   category.** The user's preferred structure is nested outline numbering
   (`1.A.2.a`) with the **chapter or beat as the top-level axis** — never a
   standalone "craft notes" bucket floating apart from the manuscript. A
   craft/technique note (pacing, reveal order, how to slow-walk a concept) still
   gets filed nested *under* the chapter it governs, as a sub-item, not pulled out
   into its own category. The output should always be building toward "which
   chapter does this become part of," never end in a free-floating meta-note.

4. **Match against the outline's beat logic, not just topic.** For each piece,
   ask which beat(s) in outline.xlsx it serves. The outline is Save-the-Cat
   structured — beats causally chain (beat 1 → *therefore* beat 2 → *but* beat 3
   complicates), not "and then this happened." Material only earns a chapter slot
   if it advances that causal chain or sharpens an existing beat's Purpose/Answer
   Key — not just because it's thematically adjacent.

5. **Flag weak chapters using the favorite-chapter test.** A chapter is under-flashed
   out if you can't picture a reader naming it their favorite. Stub chapters (notes
   only, no prose) are the clearest signal, but a drafted-but-thin chapter can also
   qualify. When new material could plausibly strengthen one of these, say so
   explicitly — that's the highest-value placement to lead with.

6. **Prioritize character and arc over mechanism.** Every named character should
   have a resolved arc, even a minor one, even if it's just getting a cup of coffee.
   When the dump mixes a science/systems idea with a character-arc idea in the same
   breath, lead with where the character material fits; the science only needs a
   one-line placement note, not elaboration.

7. **Present options, don't decide.** Where placement is genuinely ambiguous
   (could live in chapter X or Y, could be sooner or later), propose 2-4 candidate
   homes with a one-line rationale each — appended as `[Claude]`, not blended into
   the quoted material. Never pick for the user. Flag anything that conflicts with
   established canon (a character worldbuilding file, an existing plot mechanic)
   explicitly rather than silently overriding it.

8. **Never write to `manuscript.md` or `book/worldbuilding/` during this pass.** Per
   project rules, that requires the user picking an option first. Chapter working
   notes (`book/manuscript/[chapter]/notes.md`) are lower-stakes since they're
   explicitly for this kind of raw material — but still confirm before the first
   write in a given session. This command ends at an organized, lossless menu
   awaiting approval — implementation is a separate step.

## What this is not

- Not a request to draft prose.
- Not a request to finalize changes in `outline/outline.xlsx`.
- Not a place to invent new plot points, names, or details beyond what the user
  stated — organize their canon, don't extend it uninvited.
