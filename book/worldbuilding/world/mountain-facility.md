# Mountain Facility Infrastructure

**This documents the infrastructure of the [[../../timeline/refactor/legacy-humans|Legacy Human Settlement]] near [[rossland|Rossland]].**

Built using Willis Tower design principles—essentially **two Willis Towers stacked vertically** inside a hollowed-out mountain. This is where Sam does his optimization work during visits.

## Vertical Layout

**Total Depth:** 3,000 feet below surface

### Zone Structure

- 6 separate zones, each 500 feet / 40 stories
- Floor names: TBD
- Bottom level is 500 feet below sea level (aquifer level)

---

## Water Infrastructure

### The Aquifer Reservoir

Located at the bottom, 500 feet below sea level.

**Physical Description:**
- Sealed epoxy-lined basin
- Natural aquifer—the roof literally drips water constantly
- Totally isolated from external water sources
- Water marks on sides show historical levels
- Years marked on the wall

**Capacity Analysis:**
- High-water mark shows ~17 feet higher than current level
- 20 years of recorded data on the walls
- Losing approximately **3% per year**

**The Math Sam Does:**
1. Estimates room volume from dimensions
2. Calculates total capacity at high-water mark
3. Charts decline rate from year markers
4. Cross-references with regional water data

**The Discovery:**
The river fed by this mountain's snowmelt is down **10% per year**. But the climate should only account for 6-7% decline. The difference:

- **Horizontal terracing** just below the surface
- Redirects snowmelt directly into the aquifer
- They're harvesting the town's water supply
- The town never found the aquifer—they don't know this reserve exists

**Implications:**
- The facility is strangling Rossland's water source
- 3-4% of the river's decline is deliberate redirection
- The town attributes it all to climate change

### Pump System

**Booster Pumps (Primary):**
- 6 enormous pumps at the bottom level
- Second level of booster pumps at 1500 ft
- The sound is terrifying—scares the shit out of Sam when one fires
- Mike (chief engineer) laughs: "That's just the boosters"

**Jockey Pumps:**
- Every 500 feet (at each zone boundary)
- Maintain system pressure
- Keep water moving between zones

---

## Cooling Systems

### The Problem

Cooling is the **dominant engineering challenge**. 3,000 feet of compute generates enormous heat that must be extracted upward against gravity and pressure differentials.

### Zone-by-Zone Approach

Each 500-foot / 40-story block is a **closed cooling system**.

**Upper floors:**
- ~100% free cooling in normal conditions
- Economizer mode: direct outside air
- Mountain gets insanely windy, 50°F arid air, almost no moisture

**Lower floors:**
- Water-source heat pump loops
- Equipment is orders of magnitude bigger than upper floors
- Cooling demands increase dramatically with depth

### Why Closed Systems?

**Pressure isolation is critical.**

The pipes at depth are under enormous pressure. After 500 feet, the system becomes scary-pressurized. The 500-foot closed loops exchange heat upward through **enormous heat exchangers** that isolate pressure between zones.

- Gaskets would blow if systems weren't isolated
- Heat exchangers create thermal bridges without pressure bridges
- Still fails occasionally—gasket blowouts happen

### The Heat Ladder

Heat is pumped from lower to upper levels in stages, zone by zone, eventually up to hidden cooling towers.

### Hidden Cooling Towers

Located in a **hidden overhang** with good natural airflow:
- Can't be seen from above (satellite)
- Positioned for prevailing winds
- The exhaust water condenses into clouds
- Most precipitation falls back onto the mountain
- System is partially self-replenishing

### Evaporative Cooling

Upper floors use evaporative cooling:
- Enormous water usage
- Effective because air is so dry
- Draws from the aquifer

---

## Ventilation System

### Energy Recovery

Enormous exhaust fans at the top. All cooled air is captured on exit with energy recovery systems.

**How it works:**
- Compare energy (heat + moisture) of incoming air vs. outgoing air
- If incoming has more energy than the nice dry cool air being exhausted:
  - Pre-cool the incoming air
  - Heat up the outgoing air
- Net effect: don't have to re-cool incoming air from scratch

### Filter Maintenance

Robots are changing filters constantly. The place is crawling with filter-changing robots.

---

## Power Generation

### Wind Turbines

The facility operates wind farms that serve dual purposes:
1. **Power generation** for batteries
2. **Drive airflow** for free cooling

**The Interdependency Problem:**

The turbines can be adjusted like helicopter blades to raise or lower output. The RL software didn't know this.

**Sam's Key Win:**
- Below a certain CFM, free cooling isn't effective
- The system was sometimes generating less power than it cost to refrigerate
- By adjusting blade pitch dynamically, Sam optimizes the tradeoff
- Net effect: significant energy savings

### Solar Turbines

Also adjustable—another hidden parameter the RL system wasn't utilizing.

---

## Personnel

### The Mikes, Steves, and Tims

> *"If you have ever met an engineer, Sam is pretty sure there's a 35% chance he's named Mike, Steve, or Tim."*

**Key Engineers:**
- **Mike** - Chief Engineer, gives Sam the aquifer tour, laughs at him about the pumps

There are about a hundred guys named Mike, Steve, and Tim. Sam will need multiple tours with different ones to learn the whole building.

---

## Sam's Optimization Work

### Month 1: Low-Hanging Fruit
- Initial quick wins
- Surface-level improvements

### Month 2: Everything Went Up
- Efficiency metrics increased unexpectedly
- Need to understand root causes
- Requires deeper facility knowledge
- Hence: the tours

---

## Links

- [[../../timeline/refactor/legacy-humans|Legacy Humans]] - The settlement this infrastructure supports
- [[rossland|Rossland]] - The surface town, water being strangled
- [[../characters/protagonist|Sam]] - Does optimization work here
