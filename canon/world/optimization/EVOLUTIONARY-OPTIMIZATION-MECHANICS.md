# Evolutionary Optimization Mechanics - The True Parallel

## Your Constraint

**Your words:**
> "The adjustments are like the sub-goal setting or KPI setting. The intermediary loss functions. I want the book to be very true to ML algorithms. If we're using evolutionary optimization or neural net as the main mechanism (I think opt is more appropriate), what is the parallel here?"

---

## Evolutionary Optimization (NSGA-II/III) - How It Actually Works

### The Structure

**Ultimate objective:** Survive to 500+ years (DNA propagation, interstellar expansion)

**The problem:** Can't directly optimize for this (too many variables, too complex)

**The solution:** Multi-objective evolutionary optimization with intermediate objectives

---

## The Actual Algorithm Structure

### Level 1: Ultimate Loss Function (Fixed)
**Objective:** Maximize civilization survival duration + ensure expansion capability

**Measured by:**
- Years until extinction (or 500+ = success)
- Technology milestones achieved
- Population sustainability
- Resource base diversity

**This never changes.** This is the true north.

---

### Level 2: Intermediate Objectives (THE KPIs - What Gets Adjusted)

**These are the sub-goals that APPROXIMATE the ultimate objective.**

Like in multi-objective optimization, you optimize for multiple competing metrics:

**Examples:**
1. **Energy consolidation efficiency** (by year X, achieve Y joules/capita)
2. **Conflict resolution time** (average time to resolve international disputes)
3. **Innovation rate** (patents/breakthroughs per decade)
4. **Social cohesion index** (some measure of cooperation vs fragmentation)
5. **Resource allocation equality** (Gini coefficient targets)
6. **Institutional stability** (government longevity without collapse)
7. **Risk mitigation speed** (time from threat identification to action)

**These are the KPIs.** The intermediate loss functions.

**Between epochs, THESE get adjusted based on what worked.**

---

## The Selection Committee's ACTUAL Job

### What They Do

**The selected individuals analyze the trial results and answer:**

"Which intermediate objectives actually correlated with survival?"

**Example scenario:**

**Hypothesis going into Epoch 47:**
- KPI: "Maximize GDP growth" (weight: 0.8)
- KPI: "Minimize inequality" (weight: 0.2)

**Results from Epoch 47 trials:**
- High GDP growth trials: 92% died at year 118 (nuclear war over resources)
- Low inequality trials: 8% survived past 200 years

**Committee decision:**
- Flip the weights
- New KPI weighting: GDP (0.2), Inequality (0.8)
- Run Epoch 48 with new objective function

---

## The Parallel to Real ML

### In Neural Networks:
- **Ultimate objective:** Classify images correctly
- **Intermediate layers:** Learn features (edges, shapes, patterns)
- **You don't manually design features:** The network learns them
- **But you CAN adjust:** Learning rate, layer architecture, activation functions

### In Evolutionary Algorithms:
- **Ultimate objective:** Maximize fitness (survival)
- **Intermediate objectives:** Sub-goals that should lead to fitness
- **Selection:** Keep best performers based on intermediate objectives
- **Adjustment between generations:** Change the intermediate objective weights

### In This Book:
- **Ultimate objective:** Humanity survives to interstellar expansion
- **Intermediate objectives:** The KPIs (energy, conflict resolution, innovation, etc.)
- **Selection:** Individuals who succeeded on current KPIs join committee
- **Committee job:** Analyze which KPIs actually mattered, adjust weights for next epoch

---

## Why This Is "Trust The Algorithm"

### The Committee Process

**Step 1:** Algorithm analyzes 847 million trials
**Step 2:** Algorithm presents correlations:
```
Correlation Analysis - Epoch 47:
- GDP growth rate: -0.23 correlation with survival (NEGATIVE)
- Inequality reduction: +0.67 correlation with survival (POSITIVE)
- Nuclear arsenal size: -0.89 correlation with survival (HIGHLY NEGATIVE)
- Fusion energy timing: +0.71 correlation with survival (POSITIVE)

RECOMMENDATION: Adjust KPI weights as follows:
[list of numerical adjustments]
```

**Step 3:** Committee reviews
**Step 4:** Committee must decide: Trust this? Override? Adjust?

### The Tension

**Algorithm says:** "Reduce GDP growth priority, increase equality priority"

**Committee member objects:** "But GDP growth is what made our civilization powerful. We succeeded BECAUSE of growth."

**Algorithm:** "Correlation shows growth leads to resource wars. High-growth trials died at 118 years median."

**Committee:** "But... that feels wrong. Growth is good."

**The choice:** Trust your intuition or trust the data?

**The theme:** Most committees trust the algorithm. They approve the adjustments.

Like coffee guy approving patches.

**But what if the algorithm is optimizing for the wrong thing?**

---

## What Actually Gets Changed Between Epochs

### Not Changed:
- Genetic profiles of simulated humans (those are from GeneSys seed data)
- Physical laws of the simulation
- Ultimate objective (survive 500+ years)

### What IS Changed (The KPI Adjustments):

**1. Objective Function Weights**
```python
# Epoch 47 objective function:
fitness = 0.8 * GDP_growth + 0.2 * equality_index

# Epoch 48 objective function (after committee adjustment):
fitness = 0.2 * GDP_growth + 0.8 * equality_index
```

**2. Constraint Thresholds**
```python
# Epoch 47: No constraints on nuclear weapons
# Epoch 48: Constraint added: nuclear_arsenal < X megaton_equivalent
```

**3. Selection Pressure Timing**
```python
# Epoch 47: Measure KPIs at year 100
# Epoch 48: Measure KPIs at year 75 (earlier intervention)
```

**4. New Intermediate Objectives**
```python
# Epoch 47: 7 objectives
# Epoch 48: Add 8th objective: "pandemic_preparedness_index"
```

---

## How This Affects The Simulation

### The simulation doesn't change HOW humans work.

**It changes the SELECTION CRITERIA for what counts as "success."**

**Example:**

**Epoch 47 with GDP-focused KPIs:**
- Civilizations that prioritize economic growth get flagged as "high performers"
- Their strategies get studied
- Resources might even subtly favor them (if that's part of the mechanism)

**Epoch 48 with equality-focused KPIs:**
- Same starting conditions
- But now civilizations that reduce inequality get flagged as "high performers"
- Different strategies get studied and promoted

**The humans in the simulation don't know this.**

They just make choices. The system decides which choices to reward.

---

## The Committee's True Function

### They are the fitness function designers.

In a genetic algorithm, someone has to define what "fitness" means.

Usually that's the human researcher.

In this recursive system: **The selected humans from previous generations design the fitness function for the next generation.**

**The beautiful recursion:**
- Humans optimizing for sub-goals
- Best performers selected
- Those performers define sub-goals for next iteration
- Repeat

**The question:** Does this converge on the right answer?

Or does it get stuck in local optima?

(Like: "Everyone optimize for GDP" → everyone dies at year 118 → "Oh shit, that was wrong")

---

## Open Questions For You

**Q1: Are the KPI adjustments obvious or subtle?**
- Do civilizations in Epoch 48 FEEL different from Epoch 47?
- Or is it just measurement criteria changing?

**Q2: Can committee override the algorithm's recommendations?**
- Or are they rubber-stamping (like coffee guy)?
- If they can override, what happens when they're wrong?

**Q3: How many KPIs are there?**
- 5? 10? 50?
- Too few: oversimplified
- Too many: can't reason about them

**Q4: Does protagonist learn what the current KPIs are?**
- Is this part of the message/discovery?
- Does knowing change their behavior?

**Q5: Is there debate in the committee?**
- Competing theories about what matters?
- Or is everyone just trusting the algorithm's correlation analysis?

---

## Possible Reveal Scene (IDEA - NOT CANON)

**Protagonist joins selection layer. Sees the dashboard:**

```
EPOCH 847: OPTIMIZATION SUMMARY

Ultimate Objective: Civilization survival to T=500 years
Current Success Rate: 0.04%

Intermediate Objectives (Current Weights):
1. Energy_consolidation_index [0.31]
2. Conflict_resolution_speed [0.22]
3. Innovation_rate [0.18]
4. Inequality_reduction [0.15]
5. Pandemic_preparedness [0.08]
6. Nuclear_restraint [0.06]

Correlation Analysis:
[table showing which KPIs actually predicted survival]

RECOMMENDATION: Adjust weights as follows:
[proposed changes]

Committee Vote Required: APPROVE / MODIFY / REJECT
```

**Protagonist realizes:** "We're not being studied. We're being TUNED."

---

Does this match what you were looking for? The committee adjusts intermediate objective weights based on algorithm's correlation analysis from previous trials?