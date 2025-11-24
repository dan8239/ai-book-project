# How Coalescence Actually Works

## The Basic Concept

You and your sibling both got DNA from your parents. Go back one generation, your DNA "coalesces" (merges) at your parents.

You and your cousin share grandparents. Go back two generations, your DNA coalesces at your grandparents.

## How It Works: Going Backwards in Time

**Forward thinking (normal):**
- Ancestors → descendants
- One person has many descendants

**Coalescence (backwards):**
- Pick two random people today
- Trace their ancestry backwards in time
- Eventually they share a common ancestor
- That point is the "coalescence time"

## The Math

For any pair of people:
- **Recent relatives:** Coalesce quickly (siblings = 1 generation, cousins = 2-3 generations)
- **Distant strangers:** Coalesce slowly (could be 100+ generations)

The distribution follows: **T ~ Exponential(1/2Ne)**

Where:
- T = time to coalescence (generations)
- Ne = effective population size
- Larger Ne = takes longer to find common ancestors = more spread out

## Why It's Calculated Backwards

You can't predict forward (who will your descendants marry?). But you CAN trace backward:

1. Take two DNA samples
2. Compare their sequences
3. Count differences (mutations accumulate over time)
4. Calculate: more differences = longer since common ancestor
5. Use mutation rate to convert differences → generations

## Example with Real Numbers

**Two random people:**
- DNA differs at 100 locations
- Mutation rate: 1 mutation per 1,000 generations
- Calculation: 100 differences ÷ 1 per 1,000 gen = 100,000 generations to common ancestor
- Coalescence time: ~100,000 generations ago

## What Large Population Does

**Small population (Ne = 1,000):**
- Everyone related recently
- Coalescence times cluster around 2,000 generations
- Narrow distribution

**Large population (Ne = 1,000,000):**
- Some people very distant
- Coalescence times spread from 100 to 1,000,000+ generations
- Wide distribution

## The Bootstrapped Population Problem

**Real population:** Ne = 10 million
- Should see coalescence times ranging 100 to 10+ million generations
- Wide spread of genetic diversity

**Bootstrapped from subsample:** Ne = 50,000 (actual diversity available)
- Coalescence times cluster around 100,000 generations
- Everyone is "cousins" within ~100,000 generations
- Missing the deep ancestry (millions of generations back)

**The kink:** Before consolidation, they fake deep ancestry by back-calculating. After consolidation, real mutations happen. The pattern changes at the boundary.

## How Protagonist Calculates It

1. Gets archaeological CPU data (the seed dataset)
2. Compares all pairwise DNA samples
3. Counts nucleotide differences for each pair
4. Plots distribution of coalescence times
5. Sees: 100% of population coalesces to subsample at consolidation date
6. Calculates effective Ne from distribution: 50,000 (not 10 million claimed)
7. Realizes: impossible unless population was bootstrapped from subsample
