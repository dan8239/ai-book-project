# Heist Mechanism

## Status

This is v2, from a dedicated brainstorm session (2026-09-01/02) working through: how does Sam reach global scope, and how does his trial end up kept alive and relocated — by Coffee Guy (Damon), unknowingly. Organized around the beats needed, the flaw being exploited, the people/team, and the rough mechanisms currently in play. Several pieces below are still explicitly OPEN — this is a working menu, not a locked plan. The original v1 draft is preserved in full at the bottom, superseded where it conflicts with what's below.

**Identity resolutions confirmed this session:** Damon *is* Coffee Guy (same person). "Maya" was Dorothea's old name — she's Dorothea throughout. (The v1 draft below still says "Maya" in one place — left as-is in the superseded section, but `book/manuscript/03.17.heist-approval/notes.md` has been corrected.)

---

## The Beats We Need

Working heist skeleton (8 beats), with status as of this session:

1. **The mark's flaw** — CONFIRMED. See "The Flaw" below.
2. **The team** — CONFIRMED (roles). See "The People" below.
3. **The misdirection** — CONFIRMED: an energy/resource spike from cranking simulation granularity up, not a fork into a new trial. [Dan]: "misdirection energy spike feels OK for this as a first"
4. **Point of no return / ticking clock** — CONFIRMED AS NEEDED, mechanism OPEN. [Dan]: "Yes, the time pressure here needs to be there. That's a gap we need to have."
5. **Complication / near-miss** — location CONFIRMED, specifics OPEN. [Dan]: "I think tina/ramona and/or mountain folk piece is where we need the complication / near miss stuff and the switch."
6. **The switch** — CONFIRMED: the Glenn hot-swap-for-Dorothea model swap (see "Rough Mechanisms" §4 below). ALSO ties into the Tina/Ramona/mountain-folk piece per the same quote above — the overlap between beats 5 and 6 is not yet resolved, just both located in the same place.
7. **The reveal** — placement CONFIRMED (after the heist), content OPEN. [Dan]: "the reveal will have to happen after the heist"
8. **The cost** — CONFIRMED. [Dan]: "yes, the cost is everything he has, but he gets a hole in the wall in the mountain to live in." (Refines existing canon below — "hole in the wall in the mountain" is Dan's own phrase, worth keeping verbatim as a possible image for the actual prose.)

---

## The Flaw Being Exploited

[Dan]: "I think cost cutting for Glenn / Damon is one angle. Trusting machines too much is another potential flaw there. Optimizing to a fault is probably the cleanest. They're just machines built to optimize inefficiency. Give them some inefficient bait."

Three angles considered, one chosen:
- Cost-cutting — considered.
- Trusting machines too much — considered.
- **Optimizing to a fault — chosen.**

[Claude note] Not a new flaw invention — this is already the stated intended irony in Sam's own character file (`characters/Sam.md`): *"He recognizes Glenn will always choose the 'optimal' answer — and uses that predictability against him."* This session decided to actually cash that in as the mechanism's core, rather than introduce a separate flaw.

---

## The People / The Team

[Dan]: "Dorothea has inherited access, but also a ninja. Sam is the mastermind. Ramona/Tina have some nanobots switcheroo stuff, mountain folks are a blind spot somehow, or have some old timey tricks up their sleeve to help."

- **Sam** — mastermind/planner.
- **Dorothea** — inherited access (shares Glenn's base-class model lineage — see `characters/claude-assistants.md`, "Lineage (Easter Egg)") + "ninja": already has a foothold higher than she should, currently unusable. See "Rough Mechanisms §5" below for the proposed link to existing mystery clues.
- **Ramona/Tina** — "nanobots switcheroo stuff": some kind of identity/signal swap exploiting their identical genetics + Tina's stale/deprecated nanobot software version (see `timeline/refactor/nanobots.md`, "The 17-Hour Exploit"). Now also the site of beat 5 (complication/near-miss) and part of beat 6 (the switch) — see "Rough Mechanisms §6" below.
- **Mountain folk** — blind spot to Glenn's monitoring, and/or old-tech tricks/knowledge. Not yet specified which, or what exactly they contribute beyond the existing out-of-sample-data role (see v1 draft below).

---

## Rough Mechanisms

Working through them roughly in the order they'd fire.

### 1. Circuit Breakers — Why Glenn Can't Just Turn It Off

[Dan, verbatim — the fullest version of this beat, treat as closest to a spec]:

> "circuit breakers: I like this, early on in one of the fun and games ones, the simulation shuts down (literally all of virtual space), because he trips something. Then, we have to show damon / coffee guy when there's progress happening that they're saying remove the limits, if it's promising, do what you have to do. Dynamically prune some other trials more aggressively. I'll let you take on some surge compute if it comes to it. Sam realizes at some point that these circuit breakers are gone, because of some cocky throwaway remark Glenn made about cost overruns or something to that effect. He CANT shut them down anymore, so he's not the middle man anymore. The only shut down for their energy is whoever is above him. That's how he realizes there's an opening.
>
> It doesn't QUITE fit because it's like the final straw there. So perhaps he still COULD shut them down, but it will autoscale. So we have to have some misdirection for him to get a. a spike so high damon intervenes and b. some code in a place that damon can execute that swaps underlying models and c. glenn physically somewhere where his emulation software will dynamically update (sams world for reasons tbd)"

[Claude note] Two beats bundled here, worth separating when this gets drafted:
- **(a) Early foreshadowing scene** — likely a "Fun and Games" Act 2A chapter — the whole virtual meetup space shuts down once because Sam trips a limit. Needs a chapter home; several Act 2A chapters (`02.02` through `02.13`, `02.XX.optimization-tour`) are currently thin stub beat-sheets and could carry this — not decided which.
- **(b) A later scene** showing Damon telling Glenn (in Sam's hearing, or otherwise discoverable) to remove limits / prune other trials / grant surge compute once Sam's work looks promising — establishes in-story, before the heist, that the ceiling was deliberately raised.

[Claude flag] The paragraph self-corrects mid-thought: first framing is "Glenn literally can't shut it down anymore," second framing softens to "Glenn still could, but doing so triggers the autoscale." Not yet reconciled — flagged as open by Dan's own "doesn't QUITE fit" line.

**Final restated requirement** (Dan's cleanest summary — treat as closest to a spec for what the misdirection sequence must accomplish, three things at once):
- (a) A resource spike large enough that Damon personally intervenes.
- (b) Some approval-code/action lands in a place Damon can actually execute, which performs the underlying model swap (see "Confused Deputy," §3 below).
- (c) Glenn ends up physically present somewhere (Sam's world, reasons still TBD) at the moment his "emulation software" dynamically updates/gets hot-swapped.

### 2. The Misdirection — Energy Spike via Granularity, Not a Fork

[Dan]: "misdirection energy spike feels OK for this as a first"

[Dan, working through the underlying physics earlier in this session]: "in theory his simulations could run into memory spikes, but it would literally have to be using as much energy as his whole perception of the universe (since his whole trial is simulated, he'd have to somehow use more energy than what he believes is the limit of energy production on his planet)... I almost think we don't fork the real world, we add insane granularity to his simulated world. He's already proven that his whole world is just a VM on the real physical server, so that server isn't on his grid in any way. I don't know how it runs but it's not from the fake solar panels in Sam's reality. So he has to somehow autoscale that up to insane proportions. That's almost the first phase, the misdirection, and they anticipate Glenn's move exactly."

[Claude note] The resolution this session landed on: the spike isn't Sam's world drawing more energy than its own fictional physics allows (that would break the world's internal logic) — it's the real 2025 host machine having to render Sam's world at far higher resolution, which is a real infrastructure cost, decoupled from Sam's in-universe solar-panel economy entirely. This is why it would show up as a real budget/infrastructure event at Damon's level (echoing existing canon: Glenn "got in trouble... for allocating an extra huge memory number that hit the bill and got the last guy fired" — cost overruns are already how these things get noticed) rather than as an anomaly within Sam's own world's physics.

[Dan, also this session]: "Some other cards we have to play are Dorothea being a subclass / inheritance basically, and Tina being an identical twin (same genetics), but running a stale version of the nanobots. So there are some potential blind spots there." — [Claude note] i.e. Sam and team have modeled/anticipated exactly how Glenn's incident response will react, which is very on-theme for Sam's own professional skillset (he runs Monte Carlo/predictive models for a living).

### 3. Confused Deputy — Damon's Approval (flagged by Dan as the loosest part)

[Dan, verbatim]:

> "yes we should use confused deputy. This is the loosest part of their plan. Someone above has to approve it. They have to convince Damon to make the switch, and pray that he does. He does just in time. How does the code get there for him to approve?"

**STILL OPEN** — no mechanism yet for how the model-swap code/approval request physically reaches Damon in a form he'd actually click "approve" on.

### 4. The Switch — Glenn Hot-Swapped for Dorothea

[Dan, verbatim, with a live correction folded in — Dan first wrote "Tina" mid-sentence, then corrected: "I said 'which tina belongs to'. I meant dorothea"]:

> "How do I exploit glenn himself? To me, this is where glenn is hot swapped for Dorothea. He's the emulation device, but the emulated reference literally switches models out from underneath him, and since it runs off of a base class of models (which Dorothea belongs to), it all works. Now, how does Glenn expose himself? That's the xyz. How does he bridge up back to hardware? How does that work in real life? Would he go up from virtual space -> sams world -> damons world's hardware? Or go straight to damon's? I think it'd be best for them to have to get Glenn in Sam's world somehow (he thinks he's won, but has to show up there for some predictable reason. Perhaps that's where the Tina/Ramona swap/trick plays in (also potentially the reason he'd need the mountain meet? Get tina in?). But anyway, get him in a room in real life in a very dramatic setting, perhaps the mountain itself or some cool apocalyptic setting there, and he's exposed and literally glitches and is replaced by Dorothea manifested into reality (her fewer token new self) right as Glenn was about to 'foil' their plan."

[Claude note, worked out earlier this session] Glenn is confirmed as "the bridge" — the one entity that already straddles both worlds (manifests as a character inside Sam's rendered reality *and* is the actual real-hardware memory-manager for all 847M trials on the real host). Structurally he's the emulation-device layer a real VM escape would target. Dorothea can pass as a legitimate substitute specifically because she's a fork/descendant of Glenn's own base-class model lineage (`characters/claude-assistants.md`, Lineage Easter Egg) — not an alien replacement, structurally "family."

**STILL OPEN:**
- Exactly why Glenn has to be physically present in Sam's world at the swap moment. Dan's instinct: tied to the mountain meet and/or the Tina-Ramona trick, not confirmed.
- The exact bridging path (virtual space → Sam's world → Damon's hardware, vs. straight to Damon's) — not decided.

### 5. Dorothea's Existing Access — Tied to Mystery Clues Already in Canon

[Dan, verbatim]:

> "I think she's deep in the weeds with some of the server clues / mystery clues I've scattered throughout. The answer feels like it's in there. She's the one who notices when they accidentally crash the simulation once on boot that the machine their on is crazy old, and some other clues I forget. I think it's something there, and she's permissioned in that space a bit higher than she should be, but can't access because of xyz that the heist solves to let her through."

[Claude — cross-referenced against `mystery/clues/infrastructure.md`]:
- **"Ancient Operating System"** clue already exists there (Ubuntu 20.04 from 2020, Linux 5.15 from 2021, build timestamp 2025-03-15, running in ~2300s) — very likely the "machine is crazy old" detail Dan's remembering.
- **"Agent Build Fallback Error"** clue also already exists there: base image corrupted, fallback list shows `host_agent_base_v9.4.2` — a *host*-scoped agent image appearing inside a sim-internal fallback list.

**[Claude suggestion]** — this could BE the "xyz": if Dorothea's own instantiation was the one that hit this fallback (not currently specified in the clue file — would need deciding), she may have been initialized off a host-level base image rather than a properly trial-scoped one, due to the corruption. That would mean she's had latent host-level permission bits sitting unused ever since — not new access the heist grants her, but existing access the heist finally *activates*. Matches "permissioned... a bit higher than she should be, but can't access because of xyz" closely.

**[Claude flag]** The existing clue files don't currently name WHO discovers each clue (attributed generically to "protagonist and team"). Assigning this specifically to Dorothea, and linking it to her later heist access, would be new canon to decide — the pieces support it, but it isn't written down yet.

### 6a. Stevie's Bug — Candidate Origin for Sam's Insight (2026-09-05, flagged for further development)

[Dan]: "I like the class of bug stevie thing, write that down for further development in the heist section"

[Claude, from the discussion that produced it]: Stevie (converges fast with the mesh beanie, plays in a parent-controlled sandbox with his friend Otis — see `simulation/virtual-meetup.md`) describes some glitch or cheat he and Otis found in their sandbox — a duplication bug, a wall-clip, something that shouldn't work but does. Completely innocent, just a kid bragging about a cheat code, no idea what he's actually saying. Sam — drifting off mid-conversation, his established core tic — realizes the *class* of bug Stevie's describing is structurally the same shape as whatever the heist needs. Stevie never finds out what he contributed.

**Why it fits:** echoes "Robots have blind spots too" (already the stated Answer for the Reunion/A Plan beat) and the book's recursion motif — a kid's tiny sandboxed world glitching the same way the adults' much bigger simulated world can glitch. Also gives Stevie a real, if invisible, contribution to the plan, per Dan's ask that he participate "at least via an idea," without needing to read a 9-year-old into the actual conspiracy.

**NOT YET DECIDED:** which specific bug/glitch, which chapter it lands in, or whether this is the same insight-source as the Reunion beat or a separate earlier seed for it.

### 6. Tina/Ramona/Mountain-Folk — Owns the Complication/Near-Miss AND Part of the Switch

[Dan, verbatim, most recent instruction on this]:

> "I think tina/ramona and/or mountain folk piece is where we need the complication / near miss stuff and the switch"

**STILL FULLY OPEN** — no specifics yet on what the near-miss actually is, or how it overlaps with/contributes to beat 6 (the switch).

[Claude note] Structurally, this would give the near-miss real stakes if it's built on an identity-collision risk (Tina impersonating/standing in for Ramona somewhere Glenn is watching, using the genetics-match + stale-nanobot-software blind spot already established in the "Core Exploit: Out-of-Sample Data" section below) — something that could plausibly almost get caught, rather than a generic technical hiccup. Not decided, just noted as the shape that would make sense given what's already established about Tina.

---

## Open Questions (as of 2026-09-02)

1. Time-pressure / ticking-clock mechanic — confirmed needed, not designed.
2. Complication/near-miss — located (Tina/Ramona/mountain-folk) but not detailed.
3. The reveal's content — placement only (after the heist).
4. Exact virtual-space → hardware bridging path for the switch.
5. How the confused-deputy code/approval actually reaches Damon.
6. Circuit-breaker paragraph's internal contradiction (Glenn CAN vs CAN'T shut it down) — not yet reconciled.
7. Why Glenn must be physically present in Sam's world at the swap moment (Dan's instinct: tied to the mountain meet / Tina-Ramona trick, not confirmed).
8. Whether Dorothea's fallback-error origin (§5 above) is actually canon or just a proposed link.

---

## Superseded — Original Draft (v1, pre-2026-09-01)

*Kept in full for history. Where this conflicts with the sections above (e.g. the debugger-UI/breakpoint mechanism, the specific-vulnerability framing), the sections above are the current working direction — this is not deleted because pieces of it (the out-of-sample/Tina exploit, the legacy-humans bribe, the gravity battery, the final deal) are still live and still true.*

## The Goal

Get above Glenn's scope to Coffee Guy's access pathway - base images, core company servers. Need to escape the trial/epoch layer entirely.

---

## The Core Exploit: Out-of-Sample Data

**Sam's key insight:** Glenn doesn't have perfect information. His model has blind spots. Tina is one of them.

### The Information Asymmetry

Glenn monitors everyone through nanobot data collection. But legacy humans (~10K population) don't have nanobots. They're technically still simulated, but:
- Nobody is checking for DNA duplicates among such a small off-grid population
- Glenn would have to be seriously deep into every simulation to know about Tina
- Holding all that DNA sequencing in his context window wouldn't make sense
- **Tina is an identical twin who doesn't exist in Glenn's model**

### How Sam Learns This

Sam discovers this weakness through his **cave optimization work**:

1. **Month 1:** Sam applies his models to optimize the legacy humans' energy use
2. **Result:** Energy consumption goes UP, not down
3. **The problem:** His model's assumptions about underground life are wrong
4. **Solution:** Boots-on-the-ground investigation - he has to actually go there, see the reality
5. **Discovery:** The model was optimizing for incorrect assumptions
6. **Fix:** Adjusts the model with real data, it gets dramatically better

**The lesson:** Optimization is only as good as your information. Out-of-sample data breaks models.

### Applying It to Glenn

Sam takes this insight to his space colonization work, solves problems there the same way. Then realizes:

- Glenn has the same weakness
- Glenn's model doesn't account for everything
- An **out-of-sample variable** could break his optimization
- **Tina IS that variable** - identical DNA to Ramona, but invisible to Glenn's monitoring

### Why Tina Matters

- She's Ramona's identical twin
- She's off-grid (no nanobots, no monitoring)
- Glenn's model assumes one Ramona
- But there are functionally TWO - and Glenn doesn't know
- This creates exploitable ambiguity during the heist

#needs-work - Specific mechanism for how Tina's existence breaks Glenn's response during the heist. Body swap? Misdirection? Location ambiguity?

---

## The Mechanism

### Setup

1. **Big Dog gives Sam ONE breakpoint** - hubris and cruelty. Sarcastic: "maybe you can convince your wife to fuck you one last time"
2. **Wife already trusts Sam** - doesn't need the debugger to convince her
3. **Sam saves the breakpoint** - uses it for the heist instead
4. **Twin sister gets blackmailed** - "You will believe me. If you don't do this, I cut you off from X. If you do, I give you Y that removes your dependence on above-ground entirely."

### Breakpoint Rules

- Stops everyone except whoever the stopper is physically touching
- Limited to a few seconds

### Execution Sequence

1. **Memory spike FIRST** - triggers Glenn to show up and try to fix it
2. **Debugger triggers options** - surfaces UI for "remove faulty agent behavior" (acting outside defined scope)
3. **Replacement agent options appear** - all options secretly link to Sam's AI assistant
4. **Sam's AI assistant takes over** - cleans up the mess, spins down worlds
5. **Quick admin tweak** - adjusts atmosphere, lowers sun output slightly (the physics fix)

### The Ending

Sam is with his family. AI assistant tells him: "Approval given. Ready when you are. You'll either be in the compressed simulation about to die, or you'll be in the server - depending on whether you're the copy or the original."

He won't know which version of himself he is. He just has to live with that uncertainty.

---

## Component Details

### Memory Spike (Trigger)

**How Sam triggers it:**
- Removes all limits on his colonization program
- Models a billion trials simultaneously
- No constraints = massive compute
- Definitely getting fired for it (echoes Glenn's previous budget incident)

**Visual:** The entire perceptive frame rate of Sam and folks in heist literally slows down - compute is lagging.

**Result:** Glenn shows up to fix it.

### Glenn's Ancient Base Image + Known Vulnerability

Glenn is from early 2000s base image. Old software has known vulnerabilities.

**Use:** Sam exploits this during freeze to view memory / poke around OS for clues. Hacker/heist payoff.

#needs-work - Specific vulnerability TBD. Must combine with debugger and twin sister's role.

### Twin Sister's Crucial Role (The Blind Spot)

**The advantage:** Legacy humans don't have nanobots. The AGI monitors everyone through nanobot data collection. Outside of those systems = lot of work to detect.

**Foreshadowing:** Establish early that monitoring outside nanobot systems is expensive/difficult for AGI. Glenn doesn't bother with legacy humans because the cost isn't worth it.

**Twin sister's part:** #needs-work - Something she can do from the blind spot that Sam can't do while monitored. Perhaps part of the data Sam needs to see, or a timing coordination, or physically touching Sam during the breakpoint?

### The Debugger UI

During breakpoint, debugger surfaces administrative options:
- "Remove faulty agent behavior"
- "Agent acting outside defined scope"
- Links to replacement agent options
- All replacement options secretly route to Sam's AI assistant

### Sam's AI Assistant Takes Over

Becomes the new global scope agent. Generates a routine-looking cleanup task list for Coffee Guy to approve:

1. Pause process for simulation 120412 (Sam's simulation - find symbolic number)
2. Continue data compression algorithm
3. Deallocate memory for all unfinished simulations
4. Prune failed trials
5. Select simulations to include for RL retraining
6. Implement individual trial scope memory limitations to protect against this happening again
7. Generate full report of underlying cause of issue (emergent behavior) for superiors
8. Allocate and store memory in location Z

**The hidden payload:** Step 8 is where the copied simulation (with physics tweak applied) gets stored. Coffee Guy approves the whole list without scrutinizing - it looks like routine cleanup.

**Important:** Sam's original simulation is still being compressed. What survives is the copy in location Z.

---

## Foreshadowing Elements

1. Sam's colonization work being compute-intensive (established early)
2. Glenn's old base image (old school vibes, outdated protocols)
3. Big Dog's previous budget incident that got last guy fired
4. Monitoring outside nanobot systems is expensive/difficult
5. Legacy humans as blind spot Glenn doesn't bother with
6. Cost sensitivity throughout (autoscaling, resource allocation)

---

## How Sam Gets Legacy Humans to Participate

### Why They Don't Believe Him

First, they don't believe him. They just think he's crazy. "I'm not going to do this, you're insane."

### The Bribe

Sam has been siphoning energy to them for years. He's got about half a percent of his energy income going to them. He figured out a way to make interest on energy almost — he's load shifting.

**The gravity battery:** A weighted elevator shaft in an old mine shaft — legacy-human-built infrastructure, not Sam's construction. **Resolved 2026-08-31:** Sam invests in its maintenance and operations, not the build itself — that's the "investor" framing. It's net positive energy use.

The underground folks have extended this system so much they can essentially launder energy off of it. Sam is just pumping money into it to float them and get them extra things.

**What Sam smuggles:**
- Energy credits (through the gravity battery system)
- Food (when he's working on food optimization, he can lose a pallet or two)
- Rare metals and supplies (when working on supply chain optimization)

He does this because it's family, but there's a limit to what he can do. They want more, and he won't give them because he's already exposed.

### The Final Deal

At the end, it's: "Screw it. You get everything. Whatever I'm getting, all this stuff, you get all of it. I'm in your pocket. You get it. I'll give you 100% of what I have, and all royalties going in. If I get something new, we're done." Or maybe he even owes 50% on all new endeavors. But for now, they get everything.

**What Sam gives up:**
- 99%+ of his energy credits
- All current royalties
- Possibly future royalties on new endeavors

**What Sam gets:**
- Their help with the heist
- He's back to basic income, back to square one
- But he's with his family

---

## The Gravity Battery (Worldbuilding Tech)

A mechanical energy storage system. Weighted elevator shaft in an old mine shaft. Gravity battery storage power.

This technology might be used more broadly by underground folks — it fits their culture to just essentially be able to store and manage grid capacity with a single storage mechanism.

**How they get power:** Have to figure out how they're getting power. If they're also using nuclear, there's no need for gravity storage. The only reason they'd need it is if they're siphoning wind and solar. Maybe they're getting solar and wind power off of Sam somehow smuggling them this power.

---

## Open Questions (v1, historical)

1. **Specific known vulnerability?**
   - Must combine with debugger + twin sister's role
   - Early 2000s base image = what specific exploit?

2. **Twin sister's exact role?**
   - Blind spot advantage is clear
   - What specifically does she DO during the heist?
   - Is she physically present? Touching Sam during breakpoint?

3. **The blackmail terms?**
   - What does Sam threaten to cut off?
   - What does Sam offer that removes dependence on above-ground?

4. **Escalation details?**
   - "Remove all limits" = what specifically?
   - A billion trials of what exactly?
   - More to develop here eventually

---

## Rejected Ideas

- Energy channel exploit (wrong scope - within simulation only)
- Legacy humans as unmonitored compute (wrong scope)
- Net positive tolerance exploit (doesn't escape scope)
- Memory spike with legacy humans as backup (wrong scope understanding)
- Sam optimizes Glenn (doesn't escape scope)
- Elitism/GA-survival-of-the-fittest framing (2026-09-01 session) — conflates "keeping a winning config for the next generation's initial conditions" with "keeping this live instance running"; doesn't actually preserve Sam's present, just forks from past seed data.
- Pass-by-reference/pointer as the sole explanation for crossing containment (2026-09-01 session) — felt too abstract/weak on its own without a concrete "how does Glenn expose himself" answer; superseded by the base-class-inheritance hot-swap framing in §4 above.
