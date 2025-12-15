# Coalescence Theory - What Protagonist Needs to Know

## Core Concept
Trace two people's DNA backwards in time until they share a common ancestor. That point is the "coalescence time."

## The Math
**T ~ Exponential(1/2Ne)**
- T = time to coalescence (generations)
- Ne = effective population size
- Larger Ne = longer to find common ancestors = more genetic diversity

## How It's Measured
1. Compare two DNA samples
2. Count differences (mutations accumulate over time)
3. More differences = longer since common ancestor
4. Use mutation rate (~1.1×10⁻⁸ per base pair per generation) to convert to time

## The Detection Method

**Real population (Ne = 10 million):**
- Coalescence times spread from 100 to 10+ million generations
- Wide distribution of genetic diversity

**Bootstrapped from subsample (Ne = 50,000 actual):**
- Coalescence times cluster around 100,000 generations
- Everyone too closely related
- Missing deep ancestry

**The smoking gun:**
- Before consolidation: fake back-calculated history (too smooth)
- After consolidation: real mutations (proper distribution)
- Pattern changes at consolidation date = "the kink"

## What Protagonist Discovers
1. Gets archaeological CPU (seed dataset from 2025)
2. Compares current population DNA to seed data
3. Plots coalescence time distribution
4. Sees: 100% of population coalesces to subsample at consolidation
5. Calculates effective Ne: 50,000 (not 10 million claimed)
6. Conclusion: Population was bootstrapped from subsample
