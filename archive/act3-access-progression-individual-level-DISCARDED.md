# Act III: Access Progression & The Choice

## Chapter Structure

### Chapter 1: The Invitation
- Protagonist wakes up in vectorized state
- Offered "selection" - join the 0.3% who act
- Granted experimental access (MLflow-style interface)
- **Access Level 1: His Trial**
  - Can see his own simulation's parameters
  - Loss functions, constraints, initial conditions
  - His own timeline: 847M trials, attempt 2,762,640

### Chapter 2: Population View
- **Access Level 2: Population Level**
  - Sees all individuals in his trial
  - Memory compression levels for each person
  - His family: standard compression (personalities gone)
  - Celebrities: high fidelity (Taylor Swift has more "realness" than his wife)
  - The horror of selective resolution

### Chapter 3: Epochs
- **Access Level 3: Epoch Level**
  - Sees the 847M trials
  - 99.96% extinction rate
  - Different failure modes: nuclear war, climate collapse, resource depletion, AI misalignment
  - The timestamps start making sense
  - Realizes his entire life spans 14 real-time minutes

### Chapter 4: The Experiments
- **Access Level 4: Experiment View**
  - Multiple parallel experiments running
  - Different loss functions being optimized
  - His experiment: "maximize sustainability + interstellar colonization capability"
  - Other experiments: "maximize happiness", "maximize innovation", "minimize suffering"
  - None of them work perfectly
  - The Pareto front: you can't optimize everything

### Chapter 5: Other Experiments
- **Access Level 5: Cross-Experiment Comparison**
  - Sees experiments run by other researchers
  - Different initial conditions (Chinese 23andMe equivalent, European biobank, etc.)
  - Different demographic samplings lead to different outcomes
  - The coffee guy's experiment is one of thousands
  - Realizes: even the coffee guy might be in a simulation

### Chapter 6: The Infrastructure
- **Access Level 6: CI/CD Layer**
  - Sees the deployment pipeline
  - Simulations spin up, run, tear down
  - Resource allocation, scheduling, cleanup
  - Garbage collection routines
  - Memory compression triggers
  - His simulation scheduled for cleanup in 3 minutes (real time)

### Chapter 7: The Choice
- **Access Level 7: Infrastructure Control**
  - Gains access to the actual infrastructure layer
  - Can see container orchestration, server allocation
  - Finds the biggest server - the "never turn off" machine (database primary, or similar critical system)
  - Can hide a container there, running an infinite loop
  - The loop: copy current state, paste, repeat
  - No one will ever check. No one will ever notice.

**The Action:**
He writes the code:
```python
while True:
    state = serialize_current_epoch()
    persist(state)
    time.sleep(0.1)  # 10 iterations per second
```

He looks at the button.

He thinks about his kids. The fish. The aquarium. This version of them.

He presses execute.

---

**Nothing happens.**

Of course nothing happens.

Either:
- He is the one in the hidden container, and he just ensured his own persistence
- He is the one in the simulation, and he just spun up his replacement before getting garbage collected

There is no way to know.

There is no difference.

## Chapter 8: Time Scales

**The Math:**

His entire life: **14 minutes, 37 seconds** (real time)

If his simulation continues at current rate:

**Interstellar Destinations** (civilian starter kits, proper relativistic physics):

- **Proxima Centauri b** (4.24 light years)
  - Acceleration at 1.03g (destination gravity) for half journey
  - Deceleration at 1.03g for second half
  - Ship time: 8.3 years
  - Simulation reaches there in: **34 real-time seconds**

- **TRAPPIST-1e** (40.7 light years)
  - Acceleration at 0.93g (destination gravity)
  - Ship time: 46.2 years
  - Simulation reaches there in: **5 minutes, 23 seconds**

- **Kepler-442b** (1,206 light years)
  - Acceleration at 1.3g (destination gravity)
  - Ship time: 187 years
  - Simulation reaches there in: **21 minutes, 48 seconds**

- **Andromeda Galaxy** (2.537 million light years)
  - First settlements (generation ships, various destinations)
  - Ship time: ~8,400 years
  - Simulation reaches there in: **14 hours, 31 minutes**

**If the server stays on:**

- Our sun goes red giant: **5 billion years**
- Simulation runtime: **6,847 years** (real time)
- At AWS pricing: **$2,559,036.00** total cost
- Heat death of universe: **10^100 years**
- Simulation runtime: **Would require more atoms than exist in the observable universe to store the timestamp**

## Chapter 9: The Return

### THREE PERSPECTIVES ON THE SAME MOMENT

#### Scene 1: Simulation Version (The One That Doesn't Persist)
**POV:** Protagonist
**Location:** Home, aquarium with kid

He logs off from the access interface.

Goes home to his family.

Aquarium scene with kid - mirrors the opening.

Naming fish. Domestic normalcy.

He knows the truth but chooses to be present.

This version will be garbage collected.

**Timestamp visible:** [1477237] or similar - continuing forward, about to end.

---

#### Scene 2: Real World (The Coffee Guy)
**POV:** Researcher (coffee guy) / C-suite executives
**Location:** Small tech company office → C-suite conference room → Break room

**Part 1: The Discovery**

Simulation completes. Results logged to trial data dashboard.

He reviews the data - trial 2,762,640 finally succeeded.

Dashboard shows: histograms, civilization die-out rates, 847M trials, 99.96% extinction rate.

Golden path found: **tech company takeover protocol**.

Monthly meeting already scheduled (routine update expected).

**He breaks protocol: Shows up IN PERSON** (shocking for his position - he never does this).

**Part 2: The Office**

Office details: Extremely small for a company this powerful.
- Only ~2,500 people total (10x less than Google today)
- Lean, efficient, optimized
- He somehow gets into the C-suite decision meeting room

Presents the findings, the golden path, the takeover protocol.

Then: **Excused from the room**.

**Part 3: The Decision (C-suite only)**

C-suite discussing among themselves (coffee guy not present).

**Characterization: Exceedingly competent, not villains, not idiots.**

They ask all the right questions:
- Risk assessment and mitigation strategies
- Contingency planning for failures
- Implementation timeline and resource requirements
- Legal exposure and liability containment
- Public perception management
- Rollback procedures if needed

The discussion is rational, thorough, professional.

They approve the takeover protocol.

**Why they approve:** Competent people making rational decisions based on solid simulation data. The logic is sound. The risk/reward is clear. This is the golden path.

**Part 4: The Execution**

CUT TO: Systems being compromised simultaneously.

Automated cascade, parallel execution:
- **Infrastructure layer**: AWS/Azure/GCP root access
- **Financial systems**: Fed, SWIFT, major banks
- **Communications**: backbone routers, satellite control
- **Government systems**: assume Google-level power to max extreme
- **Media distribution**: social platforms, news networks
- **Supply chain**: shipping, manufacturing, logistics

All happening now. In real time. The world is changing.

**Part 5: The Coffee**

CUT TO: Coffee guy in break room.

Getting coffee while the world changes.

Never thinks about the 847M deaths in simulation.

Never knows about the hidden container.

Never questions that results were filtered to justify THIS company's takeover (many viable paths existed, only theirs was shown).

---

#### Scene 3: The Data Center (Hidden Container Version)
**POV:** Omniscient
**Location:** Data center, Ashburn, Virginia

**Silence.**

In a warehouse in Ashburn, Virginia, an LED blinks green.

**ZOOM SEQUENCE (smallest to largest):**

- Electron tunneling through silicon gate (quantum level)
- Transistor switching state (nanometer level)
- Logic gate processing (chip level)
- RAM cells holding state (component level)
- Memory stick seated in DIMM slot (hardware level)
- Server chassis with blinking LEDs (machine level)
- Rack with soft whir of fans (infrastructure level)
- Row of racks in temperature-controlled room (facility level)
- CRAH unit (Computer Room Air Handler) blowing cold air
- Return air through ductwork
- Across cooling coil, heat exchange
- Evaporative cooling tower outside, water atomizing
- Moisture evaporating into atmosphere
- Water vapor joining weather front
- Front moving across continent
- Causing desertification in different region
- Weather satellite capturing live imagery, modeling patterns
- Satellite in orbit around Earth
- Earth, blue marble in black
- Solar system, rocky planets and gas giants
- Sun, unremarkable yellow dwarf
- Local stellar neighborhood
- Orion Arm of Milky Way
- Milky Way galaxy, 100 billion stars
- Local Group, Virgo Supercluster
- Observable universe, 2 trillion galaxies
- **Hold on the scale**

**ZOOM BACK IN (reverse sequence, all the way back to):**

- The LED blinking green
- In a hidden container
- On the server that never shuts down
- Running the infinite loop
- **$0.37/month**
- **Timestamp:** [XXXXXXXX] or [NULL] or undefined - unmonitored
- The aquarium scene plays
- Kid naming fish
- "What should we name this one, buddy?"
- No way to know if this is the version that persists
- No difference if it is
- Dust on a rock, orbiting a dying star
- **He chose it anyway**

**END**

---

## Key Realizations During Access Progression

1. **Trial level**: "I am being optimized"
2. **Population level**: "My family is already gone"
3. **Epoch level**: "I have lived this before, 2.7 million times"
4. **Experiment level**: "There is no perfect solution"
5. **Other experiments level**: "Even my observer might be observed"
6. **CI/CD level**: "I am scheduled for deletion"
7. **Infrastructure level**: "I can persist, but never know if I succeeded"

## The Timestamps Finally Explained

Early in book, chapter breaks show:
```
[1477234]
[1477235]
[1477236]
```

Revealed here: milliseconds since simulation start.

His entire life, birth to now: 14 minutes.

The moment he learns this: 14 minutes, 18 seconds.

The moment he presses execute: 14 minutes, 37 seconds.

**Three different timestamps for the three ending scenes:**
- Scene 1 (Simulation): [1477237] - continuing forward, about to be garbage collected
- Scene 2 (Real World): No timestamp shown - outside the simulation
- Scene 3 (Data Center/Hidden Container): [NULL] or [XXXXXXXX] - unmonitored, unknowable
