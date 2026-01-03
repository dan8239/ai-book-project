# Optimization Hierarchy

## Optimization Goal
Minimize long-term extinction probability (NOT maximize survival time).

## Golden Path Solution
Mass nursery pods with robotic civilization starter kits sent to viable planets:
- Self-replicating
- Low individual success but high aggregate probability

**Requires:** Tech company takeover for global coordination

## The Two Levels

### 1. Per-Trial Level
**Description:** Multi-year whole world simulation (e.g. go forward from 2050, stop when extinct or clear survival beyond time window)
**Optimizes for:** Human genes surviving with redundancy (minimize total species instinction probability)
### 2. Per-Epoch Level
**Description:** Generation/batch of trials
**Optimizes for:** NSGA-II style selection from multiple trials
**Mechanism:** Evaluate which hyperparameters are associated with success. It's essentially reinforcement learning w/ global policy

## Loss Function Hierarchy
1. Ultimately it is working to minimize extinction probability.
2. It starts with certain moral constraints (no genocide, good wealth distribution, etc.)
3. Over series of unsuccessful epochs these constraints slowly get loosened by necessity
4. Successful trials start to look like this
	1. takeover event (consolidate power)
	2. automated policy (new government that is just computer driven)
	3. optimization / loss function obsessed culture
	4. genetic seeding for other planets

## Who is running this simulation?
1. This is the coffee guy running the simulation in real world
2. The epochs are batches (limited memory so you can only run so many at a time)
3. It's like a reinforcement learning job to optimize over time
4. He's been working for 10ish months on this project based on timestamp data
5. He is tweaking runs that don't converge and storing all trial data 
	1. x % survive beyond so many years
	2. key extinction reasons for each 
		1. anything that stays on earth dies eventually
		2. nuclear war / resource pressure
		3. anti-technology factions take over
		4. mass extinction events are inevitable over long enough timeframe
			1. solar flare / event?
			2. asteroids?
			3. what else could happen?

## How does simulation get discovered?
1. Protagonist needs access to global scope to see the other trials
2. He sees all of the graveyard of failed policies
3. Different [[master-parameters]]
4. We need a character that has global access to these simulations 
	1. what is his purpose? Why ever interact with a character from an individual simulation?
	2. 

