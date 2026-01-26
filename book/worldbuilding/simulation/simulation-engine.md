# The Simulation Engine

Built by [[../../world/organizations/quant|Quant]]. The crown jewel of their 23andMe research branch. Available in the present day (real world, pre-simulation).

## What It Does

Planet-level simulation with geological, weather, climate, and organism modeling. Insanely detailed. The result of years of DNA research rolled up into a hierarchical simulation system.

## The Biological Hierarchy

The engine models biology in layers that roll up probabilistically:

```
DNA → RNA → Protein → Cells → Tissues → Organs → Organisms → Populations
```

Each layer is modeled within all species' DNA sequences. The system can:
- Figure out protein folds from DNA
- Roll protein behavior up to cells
- Roll cells up to tissues, organs, organisms
- Model population dynamics from individual organism behavior

Everything is probabilistic at each layer, compounding upward.

### The Scale Problem

Consider what "modeling all organisms" actually means:
- More than **1,000 viral species** in human stool alone
- Possibly **1 million different viruses per kilogram** of marine sediment
- Most bacteriophages and viruses in these studies were **new species** when discovered

Every human gut is an ecosystem. Every handful of ocean mud is a universe of unknown life. The engine has to model all of this—not by simulating every virus individually, but by understanding the probabilistic behavior at each biological layer and rolling it up.

This is why the sprite model is essential. This is also why out-of-sample extrapolation is nearly impossible—we don't even know what exists in our own oceans.

## Memory Architecture: The Sprite Model

Think of how sprites work in video games. 100,000 fans in a fake stadium. Memory-wise, we're not creating 100,000 whole humans.

**How it actually works:**
1. There's a **base model**—one address in memory
2. This is NOT copied 100k times
3. Each frame, the 100k instances:
   - Take the base model
   - Adjust a few parameters
   - Snapshot the display state
   - Next instance does the same
4. All happens in parallel

**Applied to biology:**
- Sprites down to the DNA / cell / tissue / organism layer
- DNA sequencing rolls up to create a probabilistic organism
- DNA maps to an organism procedurally
- Everything needed to create an organism with certain traits every CPU cycle
- No need to hold full state for every cell in every organism

This is how you simulate 847 million trials of entire civilizations without melting the host machine.

## Strengths: Macro-Simulation

The engine excels at **macro-level modeling**:
- Society-level dynamics
- Species survival trends
- Population behavior over centuries
- Climate and geological processes

**Result:** Can accurately model behavior and society for a few hundred years off the current state. Given known starting conditions, the probabilistic rollup is highly accurate. Predicting whether humanity survives under certain policies? Easy. Modeling how ecosystems shift over decades? Straightforward.

## Weaknesses: Micro-Simulation of Novel Biology

The engine struggles with **building new biological organisms from first principles**:
- Emergent behavior from novel conditions
- New allele assignment for environments it hasn't seen
- Exoplanet adaptation (no training data)
- Species evolution under unprecedented selection pressures

Macro-simulation of existing worlds is much easier and more accurate than micro-simulation of brand new biological organisms. That's the gap.

This is Sam's domain. This is what he pushes.

---

## Sam's Access

As part of the colonization project, Sam requests insanely detailed simulation software:
- "I'd need this and this and this..."
- Capabilities that seem excessive for his stated project

Glenn thinks about it and decides "what the hell"—gives Sam access to the **nested simulation engine at the lower layer** (the modern-day version that can do all this).

**This is the key decision.** Glenn allowing access to the lower-layer simulation engine is what enables the necessary extrapolation of human DNA sequences for exoplanet survival. No previous trial had this capability.

**Consequences:**
1. Sam can nest simulations (run sims within the sim)
2. The lower-layer access enables out-of-sample DNA extrapolation that wasn't possible before
3. Memory allocation gets sloppy
4. Sam notices anomalies—memory pools that are impossibly large, OS timestamps that don't make sense
5. This tips him off that something is deeply wrong with his reality

## What Sam Pushes

Sam's colonization work requires out-of-sample extrapolation:
- Modifying human genome with deep sea creature adaptations
- Nuclear fallout animal genes (radiation resistance)
- Novel allele combinations that don't exist in nature
- Organisms that need to survive conditions with no Earth analog

He's essentially stress-testing the engine's weakest point—asking it to predict outcomes for genetic combinations it has never seen, in environments it has no data for.

This is both his value to the project AND what eventually leads him to discover the simulation's true nature.

## The Two-Pronged Approach

Sam doesn't solve this alone. The colonization breakthrough comes from combining two efforts:

### 1. Colony Calibration Data (Sam's Side)

The legacy human settlement data helps calibrate and tune Sam's models:
- Real population under resource constraints
- Actual survival data, failure points, energy inputs
- Ground truth to validate the engine's predictions

### 2. Cell-Level Rejection Sampling (Geneticist Colleague)

Sam's [[../../characters/co-worker-geneticist|DNA expert colleague]] pushes the envelope on out-of-sample human traits:

**The method:**
- Huge rejection sampling study at the **cell level**
- Testing plausibility of dramatic human genome edits
- Finding which deep-pressure or high-radiation sequences are **non-viable at the individual cell level**
- Then rolling up viable candidates and repeating

**The empirical work:**
- Actual human cells in petri dishes
- Extreme environmental conditions (pressure, radiation, oxygen deprivation)
- Measuring oxygen processing, DNA repair rates from radiation, etc.
- Finding extreme adaptations that cells can actually survive

**The result:**
- Identifies which genetic modifications are even possible at the cellular level
- Filters out non-viable paths before wasting simulation compute
- Provides real data to train the engine on novel biology

### The Breakthrough

The combination creates a viable path forward:
1. Colony data calibrates the macro-simulation
2. Cell-level empirical work extends the micro-simulation into out-of-sample territory
3. Together, they can model human survival on exoplanets with actual confidence

Neither alone would be sufficient. Sam does the optimization and rollup. His colleague does the wet lab work that gives the engine new training data.

---

## Technical Notes

### The Seed Data Connection

The engine bootstraps from seed data (see [[simulation-architecture|Simulation Architecture]]):
- `dna_samples_2025.db`
- `fossil_records_2025.db`
- `hospital_records_2025.db`

All the in-sample biology comes from this 2025 snapshot. The engine is only as good as its training data.

### Why Glenn Gave Access

Glenn manages 847M simulations. He's seen promising trials before. Sam's request for lower-layer simulation access is unusual but not unprecedented enough to deny. "What the hell."

The sloppy memory allocation that results? Glenn's seen worse. He doesn't realize Sam will notice the anomalies and start pulling the thread.

### Why Sam Succeeds Where Others Failed

Sam isn't special. He's just the first to get there.

The difference isn't Sam's brilliance—it's that Glenn granted access to the nested simulation engine at the lower layer. This enabled the out-of-sample DNA extrapolation needed for exoplanet survival. No previous trial had this capability.

**The implication:** Now that Glenn knows lower-layer access is what's needed, future trials will be even more successful. Sam's value has already been extracted—his specific approach can be replicated and improved.

---

## Links

- [[simulation-architecture|Simulation Architecture]] — Trial structure, time mechanics
- [[../../world/organizations/quant|Quant]] — The company that built this
- [[../../characters/Sam|Sam]] — The one who exploits its weaknesses
- [[../characters/Glenn "Big Dog" Robinson|Glenn]] — The one who granted access
