# Heist Mechanism

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

**The gravity battery:** He's invested in a mechanical energy storage system — a weighted elevator shaft, like an old mine shaft that is gravity battery storage power. It's net positive energy use. He's basically an investor in that.

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

## Open Questions

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
