# 02.XX The Optimization Tour

Sam's second visit / start of his real optimization work. He needs to learn the entire building.

## Scene Goals

1. **Start with the problem** - Month 2, everything went up unexpectedly
2. **Review low-hanging fruit** - What Sam already fixed in Month 1
3. **Reveal infrastructure depth** - The tours with Mike/Steve/Tim
4. **Aquifer discovery** - The water reservoir, the math, the implications
5. **Pump scare** - Booster pump fires, Sam jumps, Mike laughs
6. **Cooling complexity** - 6 zones, pressure isolation, heat ladder
7. **Hidden parameters** - Things the RL doesn't know about

---

## Opening: The Problem

Sam walks through his Month 1 results:
- Quick wins implemented
- Efficiency improved on paper
- Then Month 2: metrics went UP, not down
- Something's wrong with his model
- He doesn't understand the building

**The Realization:**
He optimized for local minima without understanding the system. Now he needs the full picture.

---

## The Engineers

> *"If you have ever met an engineer, Sam is pretty sure there's a 35% chance he's named Mike, Steve, or Tim."*

There are about a hundred guys named Mike, Steve, and Tim. Sam needs tours from all of them.

**Key Characters:**
- **Mike** - Chief Engineer, aquifer tour, pump scene
- **Steve** - [Cooling systems?]
- **Tim** - [Power generation?]

---

## Tour 1: The Deep (with Mike)

### The Descent

- Elevator ride down through all 6 zones
- Temperature change as they descend
- Pressure changes (ears pop?)
- Mike explains the zone system casually

### The Aquifer

**Physical Description:**
- 500 feet below sea level
- Sealed epoxy basin
- Roof literally dripping water—constantly
- Natural aquifer, totally isolated
- Water marks on the sides like a sediment core
- Years marked on the wall

**The Water Marks:**
- Dropped ~17 feet from highest level
- 20 years of data visible
- Sam does the math in his head

**Sam's Calculations:**
1. Estimates room dimensions (length × width × depth)
2. Calculates total volume at high-water mark
3. Current volume from current water line
4. Loss rate: ~3% per year

**The River Data:**
Sam already knows the regional stats:
- The river the mountain feeds is down 10% per year
- Everyone blames climate change

**The Math That Doesn't Add Up:**
- Climate should cause ~6-7% decline
- But river is down 10%
- Aquifer losing only 3%
- Missing: 3-4% going... where?

**The Discovery:**
Mike casually mentions horizontal terracing below surface. Sam connects:
- They're redirecting snowmelt
- It leaks directly into the aquifer
- They're harvesting water that should go to the river
- The town is being strangled and doesn't know it
- They never found the aquifer

### The Pump Scare

Sam and Mike are talking when—

**BOOM**

An enormous pump fires off. Sam nearly jumps out of his skin.

Mike: *laughs* "That's just the boosters."

**The System:**
- 6 booster pumps at this level (The Deep)
- Jockey pumps every 500 feet
- Second level of boosters at 1500 feet (Nimbus/Cumulus junction)
- The sound is terrifying until you're used to it

---

## Tour 2: Cooling Infrastructure

### The Problem

Cooling is the dominant engineering challenge:
- 3,000 feet of compute
- Heat rises, but they need to pump it UP
- Pressure increases with depth
- Can't run one system top to bottom

### The 40-Story Blocks

Each 500-foot zone is isolated:
- Own closed cooling system
- Heat exchangers between zones
- Pressure isolation at boundaries
- "After 500 feet, the pipes are fucking scary pressurized"

### Upper Floors (Sky Zone / Stratus)

- ~100% free cooling in normal conditions
- Mountain gets insanely windy
- 50°F arid air, almost no moisture
- Economizer mode: just use the outside air directly
- Evaporative cooling for extra capacity

### Lower Floors (Cumulus / Anvil / The Deep)

- Water-source heat pump loops
- Each 500-foot loop exchanges heat upward
- Enormous heat exchangers at zone boundaries
- "These isolate the pressure so the gaskets don't blow"
- (They still blow sometimes)

### The Heat Ladder

Heat pumped up in stages:
1. The Deep → Anvil
2. Anvil → Cumulus
3. Cumulus → Nimbus
4. Nimbus → Stratus
5. Stratus → Sky Zone
6. Sky Zone → Hidden cooling towers

### Hidden Cooling Towers

- Located in hidden overhang
- Can't be seen from satellite
- Good natural airflow
- Water condenses into clouds
- Most falls back onto mountain
- Partially self-replenishing

### Equipment Scale

- Equipment at bottom is **orders of magnitude bigger** than top
- The Deep has machines Sam has never seen before
- Cooling demands increase exponentially with depth

---

## Tour 3: Power Generation

### The Wind Farms

Dual purpose:
1. Power the batteries
2. Drive airflow for free cooling

**The Interdependency Problem:**

Yes, you should always take free power from wind. But:
- Below certain CFM, free cooling isn't effective
- You end up spending more on refrigeration than you're producing
- The RL software didn't understand this tradeoff

### Sam's Discovery: Adjustable Turbines

The solar turbines can be adjusted like helicopter blades:
- Raise or lower output dynamically
- Change blade pitch based on conditions
- The RL software didn't know this was possible

**The Optimization:**
- When airflow is sufficient: maximize power capture
- When airflow is low: reduce resistance, don't fight for marginal power
- Net effect: significant energy savings

---

## Sam's Optimization Wins

### Already Discovered:

1. **Turbine blade pitch optimization** - Adjust like helicopter blades based on airflow/cooling threshold

### To Discover (10 more):

2. **Thermal mass scheduling** - Pre-cool during windy periods, coast during lulls
3. **Cross-zone heat arbitrage** - Route heat through different paths based on zone temperatures
4. **Predictive pump staging** - Start pumps before demand spikes based on compute load forecasting
5. **Evaporative cooling water recycling** - Capture and recondense exhaust moisture, reduce aquifer draw
6. **Compute load migration** - Move workloads to cooler zones during peak heat periods
7. **Night sky radiative cooling** - Upper zones can radiate heat directly to space on clear nights
8. **Pressure differential energy recovery** - Turbines in the pressure let-down between zones
9. **Waste heat capture for heating** - The few inhabited spaces could use waste heat instead of fresh energy
10. **Seasonal aquifer level optimization** - Draw more in summer, let it recover in winter snowmelt season
11. **Altitude-based free cooling thresholds** - Each zone has different economizer setpoints, but they weren't calibrated

---

## Scene Beats

1. **Opening** - Sam reviews Month 1 wins, sees Month 2 spike, realizes he doesn't understand the system
2. **The proposition** - Needs full building tours to build accurate model
3. **The descent** - Elevator down through zones with Mike, zone system explained
4. **The aquifer** - Physical space, dripping roof, water marks, year markers
5. **The math** - Sam calculates loss rate, connects to river data, realizes snowmelt harvesting
6. **The pump scare** - BOOM, Sam jumps, Mike laughs, pump system explained
7. **The cooling tour** - 40-story blocks, heat exchangers, pressure isolation, "gaskets don't blow"
8. **The equipment** - Scale increases with depth, machines Sam's never seen
9. **The power tour** - Wind farms, cooling interdependency, turbine discovery
10. **The model** - Sam starts building his comprehensive understanding

---

## Dialogue Notes

**Mike on the pumps:**
> "That's just the boosters. Six on this level, jockeys every five hundred, second set of boosters at fifteen hundred."

**Mike on the gaskets:**
> "These isolate the pressure between systems so the gaskets don't blow." *pause* "Though they still do, sometimes."

**Sam on engineers:**
> "If you have ever met an engineer, Sam is pretty sure there's a 35% chance he's named Mike, Steve, or Tim."

**Sam on Month 2:**
> [internal] He'd optimized confidently for a system he didn't understand. Classic.

---

## How Sam Does The Work

### Learning The Systems

He has to learn all the systems of this culture. Over the next few chapters, he sets aside the colonization stuff. Maybe takes paternity leave—you get four weeks. Uses it to help them out.

He has to learn:
- Life support systems
- Aquaculture and agriculture
- The chicken stock
- Energy management
- Building control systems
- The whole mountain control system

He's getting a crash course in the rest of the space colonization problems they're working through. Learning ways to optimize those things. A better way to do his colonization project, essentially.

### Building RL From Scratch

His job is to convince them to install reinforcement learning. Takes convincing—they don't trust bringing external software onto their systems.

So he has to build it from scratch. On their old-as-fuck systems.

This is how he starts getting used to the older software. He's forced to rebuild a reinforcement learning algorithm on their ancient operating system, old libraries. Learning his way around that older shit without as much AI agent support.

### The Lobotomized AI Assistant

He gets a bastardized version of his AI assistant working on their systems. Goes back to the nearest fork that worked on those operating systems—from hundreds of years ago. Some descendant of Glenn Robinson ultimately.

It's just not the level of effectiveness he's accustomed to. He has to do more on his own, learn deeper, not rely on the agent as much. The AI agent is just complaining about how slow his brain is the whole time.

He does the work offsite on his own time. Brings it in on a fucking USB—literally the oldest shit. Has to figure out how to even get physical data into their systems because they don't have USBs. His system helps him figure it out. Gets his agent onto their network.

### Specific Wins

The RL system finds the savings:

- **VFDs modulating with stack effect** - You get natural stack effect, these fans are just balls out. They can be more aggressively tuned down.
- **CFM oversupply** - "You guys have more CFM flowing through here than you need"
- **Loosen temperature controls**
- **Reduce lighting**
- **More aggressive scheduling**
- Whatever else—just figure out how heating and cooling works in this thing. The lower you go, the hotter it is.

---

## The Emotional Arc

### What Sam Can Buy Them

He can probably increase the energy diversion to 3-4% without anybody noticing. Can buy them two years. Three years. Maybe 20 or 30 years with enough optimization. He can buy them enough years.

### Ramona's Daydream

Ramona starts daydreaming about moving down here. A few conversations about it—people she knows who've gotten rid of their chips, moved down, moved with the family, moved with the kids.

Sam hasn't told her the real mission at that point. It starts to seem like that's the ending—they move underground.

### Sam's Confession

Sam comes clean on the whole actual reason for the colonization project. Comes down with the fact that it doesn't matter.

"Everything I'm doing doesn't matter. Yes, I'm giving them more time. I'm fulfilling this contract. I can even get them up to 3-4% of my income without anybody noticing. I can buy them two years. Three years.

But the problem is the whole thing is doomed. Not only that—we're doomed. This family we're in. The ones above, the ones below, everyone. This is not going to get better.

There's no solution here. The food will dry up. They'll run out of topsoil. All the bad shit from the space colonization research."

### The Fallout

This creates conflict. Falling out with Ramona. Iciness. He shattered her daydream and told her there's no escape—not above, not below.

---

## Links

- [[../../worldbuilding/world/mountain-facility|Mountain Facility Infrastructure]]
- [[Sam|Sam]]
- [[../../worldbuilding/world/rossland|Rossland]]
