# Honeycomb

**Era:** [[../timeline/sim-present|Sim Present (~2125)]]

The global governance system that replaced nation-states after [[../timeline/refactor|The Refactor]].

## Structure

### Geospatial Hierarchy

Honeycomb uses **H3** (Uber's hexagonal hierarchical spatial index) to organize all governance. The hex grid replaced countries, counties, and municipalities entirely.

- **Resolution 0-15**: Each hex contains 7 child hexes, creating nested governance layers
- **No borders**: Just resolution levels—zoom in for local, zoom out for regional
- **Equal neighbors**: Every hex has 6 equidistant neighbors (no awkward corners)

### Nodes

At each hex resolution level, there's a governance node consisting of:

| Role | Type | Function |
|------|------|----------|
| **Driver** | AI | The AI portion of the node. Manages resources, calculates ROI, decomposes tasks, interfaces upward |
| **Controller** | Human | The human portion. Represents human interests, makes judgment calls, provides ground truth |

Driver and Controller are equal but necessary—neither outranks the other.

### Hierarchy

The entire governance system is a **nested AI agent**. A single governing entity decomposes into smaller and smaller units:
- Global scope → Continental → Regional → Local → Neighborhood → Family → Individual
- Each level has its own Driver/Controller pair
- Drivers share state across scopes (a regional Driver knows what its child Drivers are doing)

### Family Units

Yes, even families are governance nodes:
- Every family has a **family Driver**—a general-purpose AI rep for that household
- Individuals report upward through family structure
- Families still function normally day-to-day; the structure is administrative

## Economy

### Open Source Model

The economy runs on an open-source contribution model:
- People publish projects (repos)
- If a project gets picked up (used by Honeycomb), you get **1% of energy savings** generated
- Everything is quantified by **M&V** (Measurement & Verification)

### M&V System

All value is measured through automated energy savings validation:
- Canary releases
- A/B testing
- Baseline / counterfactual modeling
- Representative sampling
- Out-of-the-box billing

*Note: [[Sam|Sam]] built the M&V system. He's wealthy from royalties on it.*

### Job Market

The job market is a centralized matching service:
- Drivers calculate expected energy savings vs. time-to-implement (ROI)
- Drivers request resources/labor for projects
- Humans apply for positions
- It's matching, not hiring—you take contracts, not jobs

### Contract Types

1. **Controller positions**: Short-term human representation at a node
2. **Project work**: Requested by Drivers, humans apply and execute
3. **Open source**: Publish your own projects, get funded/forked if useful

### Energy as Currency

Everything is charged by energy use footprint. All data usage — phone texts, asking a question on your phone — your energy use footprint is basically how much money gets spent. Burgers are just literally converted to some rough order of magnitude CO2 equivalency. That's the unit of getting charged for things.

Everything you do just gets charged, like token usage, because you use your phone, there's some device in the cloud that is literally running to serve this. So you get charged your energy use.

### Access Tiers

The base human level survival kind of usage covers day-to-day stuff that's normal. The fact that someone works gives them a feedback mechanism of more access to more advanced ML. It's just a feedback reinforcement loop that's slowly separating the species from post-human and regular human.

This is why Sam has access to the things he does — his work generates enough value to afford advanced AI tooling that regular humans don't get.

### What's Covered vs. Luxury

**Existence bill (covered by UBI):**
- Life support
- Food
- Healthcare
- Education

**Luxury (pay-per-use):**
- You drive a car, you pay for the kilowatt hours to charge the batteries
- You use a building, the time you're in there, the energy use of that building is split amongst all occupants
- Using the internet — when I say internet, I mean the clouds. When you're in the clouds, simulating — that's a luxury. That's an expensive compute situation that your life support budget doesn't support. You're not on there unless you're working, basically.

### Inheritance

Stuff is non-transferable for adults. The inheritance tax here is basically almost a use it or lose it. There's no passing down to your kids kind of deal.

You almost donate your energy reserves to a cause you're interested in. You're financing a charity of your choice, essentially, when you pass on.

There's ways to funnel that to your kids in a way, but ultimately, if the kids are not working, not a Controller on a project, they're not getting energy credits.

### M&V Details

How it actually works:
- Real time usage tracking
- Workers get real time savings
- It's always: baseline → performance → savings
- For things before and after implementation
- A/B tested, phased rollout across populations

This is how Sam actually makes money — not the food stuff. The M&V system. Food is just a line item in your costs.

## Sam's Relationship to Honeycomb

[[Sam|Sam]] is unusual in this world:
- Built the **M&V system** that underpins all economic measurement
- Takes **Controller positions** on short contracts (has been a local hex Controller, family Driver, other contracts)
- Posts **open source projects** that sometimes get funded/forked
- Current contract: **Food chain optimization**
- Still does **human→machine projects**: prototypes solutions that get picked up and maintained by AGI
- Gets **royalties** when his projects scale

He's rare because most people just work on AI-originated projects. Sam still originates work that AGI adopts.

## Glenn's Role

[[../characters/Glenn "Big Dog" Robinson|Glenn]] is the **Driver** for the [[../simulation/colonization/colonization-program|colonization project]]—that's his formal relationship to Sam.

But Glenn is different from normal Drivers:
- He's at **global scope**—manages 847M simulation trials
- He **shares state** with thousands of instances of himself across local and global scopes
- He's essentially distributed—a "god" in terms of capability within the simulation
- Normal AI agent rules don't apply to him (he predates them)

## A/B Testing Infrastructure

The reason that it's hexes and everything is divided into grids is because A-B testing is part of this world. It's dividing the entire populace into equal-sized areas that can be studied with extensive statistical testing across many different policies and this is essentially how the whole policy is being driven — through statistical analysis of the population.

They're testing things — figuring out which DNA genomes are responsible for certain behavior. Correlative studies. They're mapping the whole human genome basically, but more detailed with trait level specifics, and that's how they're doing it.

The researchers are learning from this data. The policy in each simulation is being formed by this and they're literally injecting randomness into each hex so they can statistically study the differences in the hex, find out more about the genome, find out causally what policies lead to what behaviors. It's almost just — split the sample into representative demographics and learn from them.

They're also trying to isolate populations intentionally and do decades-long research about isolated populations. Think of it as the ghost populations of humans — they've found that we're starting to speciate. It's that level of genetic drift they're intentionally manufacturing as part of this.

That has to be a theme. That should be how Sam solves the problem — by using that data.

At the Damon level: they're using the same methods — statistically balancing across so many civilizations that they can actually derive real correlation.

**See also:** [[../themes/themes|Core Themes]] — A/B testing as a supporting theme across the book.

## Branding

Honeycomb is global government with good PR:
- Named after something sweet, natural, cooperative
- Implies collective benefit (bees making honey together)
- Hexagonal logos, golden color palette
- "I work for Honeycomb" sounds like a tech company, not a dystopia
