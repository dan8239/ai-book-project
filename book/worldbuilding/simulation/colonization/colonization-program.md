# Project Te Waka Ora

**Alias:** Project TWO (double meaning — the second try of human civilization)

The space colonization effort. Not expansion — escape.

Named for the Polynesian voyagers who colonized the Pacific islands, carrying portable ecosystems in their canoes — taro, pigs, chickens, dogs. They didn't just move people; they moved entire biospheres.

## Why Colonization Exists

See [[extinction-trajectory#The Guillotine (Classified Knowledge)|The Guillotine]] for full context.

- **Public story:** Mars colonization has already happened. It's just a science experiment out there. A few thousand moles living underground scraping microbes off of tunnel walls. How could they pull from the food chain division for that?
- **Classified truth:** Earth is a write-off. Ozone collapse is coming. Colonization is the only path where humans survive at all. Mars needs insane terraforming — thousands of years, not nearly enough time, still dependent on imports from Earth. Mars is dead too.

## The Program

### What They're Doing

Mass nursery pods sent to viable planets:
- Self-replicating systems (on-arrival, not in-transit)
- Low individual success rate but high aggregate probability
- Hundreds of parallel payloads per launch wave

### The Math (Moral Quandary)

- Success rate per colony mission is decent (protagonist optimized it)
- But species survival requires X target colonies for redundancy
- To hit six sigma species survival, you need parallel attempts
- Each launch wave requires enormous energy/resources
- **The resource extraction would kill a huge percentage of Earth's remaining population**

Trade-off: optimize for species survival = sacrifice current humans. [[../characters/protagonist|Protagonist]] is asked to run the numbers on how many people die so the species might survive.

---

## Mission Te Waka Ora — The Spec

### Target

**Alpha Centauri**, 4.3 light years. Both Alpha Centauri A (G2V, sun-like) and Alpha Centauri B (K1V) host candidate planets in the habitable zone. The mission targets two rocky planets, one per star, for redundancy and eventual species divergence.

### Launch Wave

Each launch event releases **hundreds of parallel payloads** through the same laser slingshot. They share the launch infrastructure but separate in flight, each aimed at its own target. Alpha Centauri is the lead destination; further targets come from [[#Starglass Technology|Starglass]] surveys.

**Recursive seeding:** every payload carries instructions for repeating the mission once its colony matures. Each successful colony eventually becomes a launch site for the next jump. The program scales like an exponential, not a linear push.

### Timeline (Earth-frame, per payload)

| Phase | Duration | What happens |
|---|---|---|
| Laser burn | ~1 yr | Home-system laser array gently accelerates payload to 0.05c (~0.1 g sustained over months) |
| Coast | ~86 yr | Sail furled, payload dormant, RTG keeps critical clocks alive |
| Photogravitational brake | ~10–20 yr | Sail flips; Alpha Centauri's starlight pushes back, gradually shedding speed |
| Orbital capture | ~1–5 yr | Gravity assists off the binary stars + sail trimming into orbit around the target planet |

**Total:** ~100 years Earth-time. Time dilation at 0.05c is negligible (γ ≈ 1.00125 — travelers would age about six weeks less across the century). This is unambiguously a multi-generational mission for any humans involved; nobody who waves goodbye sees the arrival.

---

## Propulsion

**Home-system laser pusher for launch; the destination star's own light to brake.** One sail, three jobs:

1. **Pusher target** during the laser burn (months-long gentle push, not a Starshot 10,000-g kick)
2. **Brake** during the deceleration phase, flipped to face Alpha Centauri
3. **Parachute** for atmospheric descent at the very end

The 0.05c cruise speed isn't set by what the laser can deliver — it's set by what the destination star can brake. Come in faster and the photogravitational force can't shed your velocity before you blow past the system. Slower is fine; faster is impossible.

**No onboard propellant. No nuclear engine.** The energy budget is asymmetric and well-understood: gigawatts at launch, almost nothing thereafter. The arrival side of the mission costs essentially zero energy compared to getting there.

---

## Payload Manifest (~50 lb / ~23 kg per pod)

Nothing biological travels alive. The cargo is inert, solid-state, and stable for centuries.

| Component | Mass est. | Form | Purpose |
|---|---|---|---|
| Caretaker units (5) | ~5 kg | Powered down, shielded, rad-hard | The crew — see [[#The Caretakers|below]] |
| Mechanical printer | ~3 kg | Polymer/composite/electronics fabrication | Builds and repairs caretaker bodies |
| Bio synthesis unit | ~2 kg | Microfluidic chemistry rig | Activates synthetic founder cells, assembles genomes |
| Silica genome library | ~0.5 kg | Glass storage cube, palm-sized | Every species' genome + full human cultural archive |
| Synthetic dormant founder cells | ~1 kg | Engineered spore-state, vitrified | Biological seed stock — see [[#From Synthetic to Biological|nuance below]] |
| Chemistry feedstock | ~5 kg | Dry crystalline amino acids, nucleotides, lipid precursors, polymer monomers | Raw material for first synthesis runs (both mechanical and bio printers) |
| Sail + hull | ~5 kg | Graphene-membrane sail (folded), polymer composite shell | Propulsion, micrometeoroid shielding |
| Radiation shielding | ~1 kg | Water ice or polyethylene layer around sensitive electronics | Doubles as arrival-day resource |
| Power | ~0.5 kg | Small RTG + solar deployment | Centuries of trickle power, then sunlight at arrival |

---

## The Caretakers

**Five units. A Maori creation pantheon.** Mechanical, not biological — they must arrive functional on day 1, because nothing on the planet yet exists to grow them from.

### Design

- **Woven polymer-thread musculature** — twisted-coil actuators, McKibben-style. Light, repairable, printable strand by strand. Looks more like rope-and-fabric than metal-and-servo.
- **Lightweight polymer skeleton.** Printable.
- **Photovoltaic skin.** Their outer surface is their power source.
- **Sensors:** optical (eyes), tactile on extremities, chemical analysis for soil/water/atmosphere.
- **Shared distributed mind across all five units.** Each body has a local rad-hard processor, but they run a single networked intelligence — continuous memory replication, consensus over key decisions. **Loss of one unit = loss of redundancy, not loss of self.** The *individual* is the network.

### Transit Hardening

- **Powered down completely** during the 86-year cruise. No metabolism, no wear.
- **Stored in the lander hub** behind whipple shielding (micrometeoroids) and a water-ice/polyethylene layer (radiation).
- **Rad-hard FPGAs or memristor arrays** with triple-modular redundancy for brain hardware.
- **Silica storage** for the archive and the shared mind's persistent memory.
- **RTG-trickle power** keeps wake circuits alive across the century.
- **Solar trigger** on arrival: sail deploys, light hits the skin, system boots.

### Self-Repair and Replication

The mechanical printer builds new bodies or replacement parts from feedstock. Early on: dry chemistry from the transit cargo. Later: bio-derived polymers (cellulose from plants, chitin from insects, bioplastics) once the biome can supply them. **Their population is gated by what the planet can afford** — same constraint as everything else in the mission.

The shared mind clones into new bodies as they're built. New units inherit full memory and history.

### The Five

| Unit | Domain | Mission role |
|---|---|---|
| **Rangi** | Sky father | Orbital hub / comms relay. Literally stays in the sky — never lands. Coordinates the surface units, holds the master archive, relays signals back to Earth and (eventually) outward to future colonies. |
| **Papa** | Earth mother | Soil tier — microbe and fungi seeding, ground readiness assessment. The first to land. Patient. |
| **Tāne** | Forests, light, life-bringer | Plant tier — mosses → vascular plants → forests. The deity who pushed his parents apart to let light in; here, the one who builds the canopy. |
| **Tangaroa** | Oceans, water | Hydrology, water cycle, marine seeding. Works the coasts and waterways. |
| **Whiro** | Darkness, death, decay | The decomposer / cycle-of-death role — necessary for any real ecosystem. Also the **dissident** unit. Mythologically Tāne's dark twin, made from leftover materials, banished after losing the contest for the heavens. Here: the one who pushes back on consensus, the built-in skeptic, the part of the system that questions whether they should be doing any of this. |

---

## The Build Ladder

Seven rungs. Each waits for the previous to transform the soil and atmosphere. Caretakers seed and observe — they don't terraform, they don't farm. They time the next release.

1. **Microbes / cyanobacteria** — make soil, fix nitrogen, generate oxygen
2. **Fungi + simple plants** (mosses, lichens) — break rock, deepen soil, partner with plants
3. **Vascular plants** — real food base, atmospheric maturation
4. **Invertebrates** — pollination, decomposition, soil turning
5. **Small vertebrates** — fill out the food web
6. **A primate species** — **unskippable.** No artificial wombs travel. Humans need a mother. A closely-related primate is seeded first to establish a breeding population that can gestate and first-rear the human tier.
7. **Humans**

Decades pass between rungs. Soil maturation, forest succession, atmospheric oxygenation — none of these can be rushed by technology.

---

## From Synthetic to Biological

**The nuance:** "synthetic" cells in this era means *assembled from chemistry, not inherited from a parent cell*. Same building blocks as life (DNA, proteins, lipids — because that's what works), but no biological ancestry. The advantage for transit is that you can engineer them in ways evolution never bothered:

- Membranes from extremophile-grade lipids — far more stable than any natural cell
- DNA stored in a glass-like crystalline matrix inside the cell
- Pre-built ribosomes locked in a quiescent state
- No live metabolism that would decay across the century

A synthetic dormant founder cell is essentially a designed-from-scratch spore. The **bio synthesis unit revives them on arrival** and bootstraps the tree of life from there:

1. Wake synthetic prokaryote founders → they divide → real biological prokaryotes
2. Bootstrap the first eukaryote by endosymbiosis — synthetic prokaryote + installed synthetic organelles + synthetic nucleus (mirrors how eukaryotes actually evolved on Earth)
3. Founder cells/seeds/zygotes for each species at the appropriate build-ladder rung
4. Normal reproduction takes over once a founder generation exists

The "synthetic" label only applies for the first couple of cell divisions per species. After that it's biology copying itself for free.

---

## Starglass Technology

Pioneered in Mars orbit. Makes detection of Earth-like planets (small, rocky, orbiting yellow dwarfs) much easier.

**The streetlight effect:** asked why, on a dark night, he was looking for his missing car keys beneath a street lamp, the man answered, "because the light's better."

We found plenty of planets under the street lamp because red dwarfs let you see the planets around them. Now we can actually search beyond the street lamp.

- **Before Starglass:** most discovered exoplanets orbited dim red dwarfs. Hundreds of "Earth-like" planets found, but tidally locked, blasted by radiation, not viable.
- **After Starglass:** previously undetectable exoplanets discoverable at huge scale. This is what gives the program enough Sun-like targets to justify the parallel-launch wave strategy.

**Why Alpha Centauri specifically:** closest sun-like star (4.3 ly), binary system with planets around both A and B, lets the mission seed two slightly different worlds from a single launch wave. Distance also makes it the only target where the 100-year envelope is even plausible.

---

## Protagonist's Contribution

### The Original Ask

Optimize survival for 2–3 specific planets. Niche problem.

### What He Finds

- He can raise survival rates on those specific planets much higher
- But most failure cases aren't at the destination — they're in transit, landing, or planet viability uncertainty
- Optimizing for 3 perfect missions misses the point

### The Multi-Part Insight

1. **Resource allocation:** quantity > quality on similar vectors. 30 "good enough" missions beats 3 "perfect" ones.
2. **Generalized payload:** start with generic synthetic-cell payload + extreme genetic variation in the archive instead of planet-specific optimization. The bio synthesis unit samples and generates the right founder cells in-flight or on arrival.
3. **Don't waste the launch infrastructure:** the laser slingshot is the expensive part. Once it's lit, push hundreds of parallel payloads through it, not three.

### Why Him

His food chain optimization background — he's used to thinking about yield across uncertain conditions, redundancy, and resource allocation. The space specialists were optimizing the wrong thing.

---

## The Moral Cost

- **Original approach (Mars terraforming):** change the planet to fit humans. Long and hard. Planets take forever to change.
- **His realization:** biology doesn't. Biology is flexible.
- **Government policy:** "Humans and their descendants survive." That's the constraint. Not "humans as we know them."

**What he builds:** seed payload with founder cells for flora, fauna, humans. But by the time it's morphed into something that survives the target planet, it's hardly recognizable. Descended from us, selected from our ecosystem, but post-human.

**The question:** is humanity "saved" if what survives isn't recognizably human?

**The deeper question (cultural):** the first humans born on Alpha Centauri arrive into a world with no parents, no language, no fire, no norms — gestated by primates, raised by the caretakers and the archive. Do the caretakers transmit culture, or do they step back and let it emerge feral? This is the cultivated-vs-wild tension the Maori pantheon already carries — and the philosophical core of the mission.

### Why This Approach Works at All

**Can't you just fix Earth?**

See [[post-refactor-society#Why Genetic Modification Can't Save Them|Why Genetic Modification Can't Save Them]]

- H₂S blocks cellular machinery in ALL aerobic life
- Would need to redesign electron transport chain (fundamental biochemistry)
- Would need to do it for ALL species simultaneously
- Can't rebuild an entire ecosystem while it's collapsing

**Colonization is different because:**
- Starting fresh with a newly-built biosphere
- Not fighting a poisoned, collapsing system
- Can engineer FEW species for new environment

---

## Timeline

| Phase | What Happens |
|---|---|
| **Protagonist's era** | Active program, launch waves leaving, genetic payloads being optimized |
| **Discovery** | Protagonist needs more genetic diversity, finds weird dataset in 23andMe-type DB |
| **Moral choice** | Must make callous decision for colonization (TBD — morph DNA beyond recognition?) |
| **Technical solution** | Technically solves colonization optimization |
| **The horror** | Learns epoch is ending, world will be erased — his work doesn't matter |

## Connection to Mystery

1. Working on colonization genetic payload
2. Government seed data has bottleneck problem — effective population too small
3. Needs older / more diverse genetic strains
4. Looks for specific datasets — relatives, extinct variants
5. Finds weird dataset — wrong location, old format, not properly ingested
6. This is where [[../characters/devsecops-woman|DevSecOps woman]] planted the message

## What Big Dog Is Watching

From [[../characters/Glenn "Big Dog" Robinson#Why He's Watching Protagonist|Big Dog]]:

Protagonist is getting close to the moral breakthrough needed for colonization success. Most of 847M trials fail at this point. This epoch has promising trials that will snowball results.

---

## Open Questions

#needs-work

**Atmospheric descent.** The lander has to get the caretakers and printers to the surface intact after 100 yr in deep space, through an atmosphere we won't know the composition of until approach. Sail-as-parachute is the working idea but needs detail — heat shield? Staged braking? How does Rangi separate and stay in orbit while the others descend?

**Cultural transmission.** Cultivated vs. wild — guided culture from the archive, or let the first humans emerge feral over generations? This is the philosophical core but the mechanism isn't designed yet. Likely a Rongo/Haumia-style internal disagreement among the caretakers in narrative terms, even though those two aren't in the roster.

**Whiro's role on the ground.** Dissident built into the system is great in concept; what does he actually *do* during the build phase? When and how does his disagreement express itself? Plot fuel.

**Mass budget verification.** The ~23 kg total is plausible at order-of-magnitude but each line item needs sanity-checking, especially the 5 caretakers at 1 kg each — that may be optimistic.

**Original moral question (kept):** what specific moral choice is required for colonization? What percentage of Earth population dies for the resource extraction to fund the launch waves?

---

## Manuscript Contradictions to Reconcile

The current draft of the [[../../../manuscript|Space Onboarding chapter]] has earlier mission language that conflicts with this spec. Per project rules, the manuscript stays untouched until you're ready to revise it. Items to fix when you do:

- **"two small modular reactors"** → solar + small RTG. No fission onboard.
- **"Raw organic material for printing"** → dry chemistry feedstock only; no organic cargo.
- **"two bio-printers with incubators"** → bio synthesis unit, no incubators (primate tier is the womb).
- **"refrigerator size"** → spec is ~50 lb / briefcase-scale per pod, not refrigerator-scale.
- **"Each has a sail"** in pod notes → consistent with this spec (each parallel payload has its own sail), keep.
- **Caretaker count and names** → notes list Fuxi/Nuwa or Rangi/Papa as candidates; locked roster is **Rangi / Papa / Tāne / Tangaroa / Whiro**.
