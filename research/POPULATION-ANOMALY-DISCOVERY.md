# Population Anomaly Discovery Method

## The Setup

**Bootstrapping quality:** Sophisticated and mostly correct
- Proper recombination rates applied
- Realistic haplotype structure maintained
- Demographic history simulated accurately
- Mutation rates correct
- Population structure looks right

**The flaw:** Not in technique, but in fundamental limits of what's possible from finite sample

## The Discovery Method

### Timeline Context

- **Consolidation (Year 0):** Simulation starts from 1M samples (2025 genetic data)
- **Protagonist's time (Year 100+):** 100+ years of simulation running
- **Real mutations:** Accumulating naturally during simulation runtime

### What Protagonist Calculates

**Step 1: Rare variant age distribution**

Count rare variants (< 0.1% frequency) and calculate their age from frequency + mutation rate.

**Expected distribution (real 100,000 year population):**
- Most variants: very old (thousands of generations)
- Some variants: recent (last few generations)
- Smooth exponential distribution across all ages

**Actual distribution (bootstrapped population):**
- Cluster 1: ~90% of variants date to consolidation (Year 0)
- Cluster 2: ~10% of variants from last 100 years
- **Missing:** All the variants from deep time (1,000-100,000 years old)

**The graph:** Bayesian skyline plot shows population "appearing" at consolidation instead of smooth ancient history

### Step 2: Total rare variant count

**Expected (8 billion people, 100,000 year history):**
- ~10^8 total rare variants across population

**Actual (bootstrapped from 1M samples + 100 years):**
- ~10^6.1 rare variants total
- **Missing 99% of expected rare variation**

### Step 3: Archaeological CPU comparison

Gets access to seed dataset (the 2025 samples used to bootstrap simulation).

**The smoking gun calculation:**
"What percentage of current rare variants trace directly to seed data?"

**Answer:** ~90%

**Impossible because:**
In real population, most rare variants either:
- Predate the seed samples by thousands of years, OR
- Appeared in last few generations (post-seed)

Having 90% trace TO the seed samples means population was created FROM them.

### The Graphs That Show The Anomaly

**Graph 1: Bayesian Skyline Plot**
- Shows effective population size over time
- Should show smooth ancient history
- Instead: population "appears" at consolidation date
- Discontinuity impossible to explain

**Graph 2: Site Frequency Spectrum / Rare Variant Distribution**
- X-axis: Variant frequency (how rare)
- Y-axis: Count of variants at that frequency
- Expected: Smooth exponential curve with long tail
- Actual: Missing the ultra-rare variants (< 1 in million)

**Graph 3: Variant Age Distribution**
- X-axis: Age of variant (generations)
- Y-axis: Count of variants that age
- Expected: Smooth distribution across all ages
- Actual: TWO CLUSTERS (consolidation + recent), missing middle

## Why This Takes Time To Discover

**Other explanations protagonist eliminates first:**

1. **Population bottleneck:** Could explain reduced diversity, but not the age clustering
2. **Selection sweep:** Could remove variants, but not create the two-cluster pattern
3. **Data quality issues:** Could explain missing variants, but not the perfect clustering at consolidation
4. **Sampling bias:** Could affect counts, but not the age distribution pattern

**The process:**
- Initial observation: "Diversity seems low"
- Test bottleneck hypothesis: Pattern doesn't match
- Test selection hypothesis: Wrong signature
- Check data quality: Data is fine
- Finally: "Wait, why do 90% of rare variants date to exactly consolidation?"
- Gets archaeological CPU data
- Confirms: They all trace to the seed sample
- Conclusion: Population was bootstrapped

## Key Point

The bootstrapping technique itself is excellent. The variants look real, haplotypes look real, mutation rates are correct.

The flaw is fundamental: **You can't create 100,000 years of genetic diversity from 100 years of real mutation + reshuffling a finite sample.**

The missing rare variants and the age clustering at consolidation are inevitable consequences of bootstrapping, no matter how sophisticated the method.
