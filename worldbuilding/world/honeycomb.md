# Honeycomb

**Era:** [[../timeline/sim-present|Sim Present (~2225)]]

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

*Note: [[../characters/protagonist|Sam]] built the M&V system. He's wealthy from royalties on it.*

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

## Sam's Relationship to Honeycomb

[[../characters/protagonist|Sam]] is unusual in this world:
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

## Branding

Honeycomb is global government with good PR:
- Named after something sweet, natural, cooperative
- Implies collective benefit (bees making honey together)
- Hexagonal logos, golden color palette
- "I work for Honeycomb" sounds like a tech company, not a dystopia
