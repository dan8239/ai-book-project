# Coalescence Time Graphs - The Visual Evidence

## The Primary Graph: Bayesian Skyline Plot (BSP)

### What It Shows
**Effective Population Size (Ne) vs Time**

### Axes:
- **X-axis**: Time (years before present) - typically LOGARITHMIC scale
- **Y-axis**: Effective population size (Ne) - often LOGARITHMIC scale as well
- **Units**:
  - Time: years or generations before present
  - Population size: Ne (effective population size, not census size)

### What It Looks Like:
- **Smooth curves with confidence intervals** (shaded regions showing uncertainty)
- Line represents median effective population size at each time point
- Based on coalescence times calculated from genetic sequences

### The Key Insight:
Population size changes over time create different patterns in coalescence times:
- **Population expansion**: Coalescence times bunch up (many recent common ancestors)
- **Population bottleneck**: Coalescence times show gap/compression
- **Constant population**: Exponential distribution of coalescence times

## The Graph You Need: Pairwise Coalescence Time Distribution

### What It Shows
**Distribution of when pairs of sequences shared common ancestor**

### Axes:
- **X-axis**: Time to Most Recent Common Ancestor (TMRCA) in generations or years
- **Y-axis**: Frequency/Probability density
- **Scale**: Can be linear or logarithmic depending on time depth

### Expected Pattern (Normal Population):
Under standard coalescent model:
- **Exponential distribution** with rate parameter 1 (in units of 2Ne generations)
- Formula: P(T) = (1/2Ne) × e^(-t/2Ne)
- **Noisy/stochastic** - real data shows variation around expected curve

### What Bootstrapped Population Would Show:
**DISCONTINUITY AT CONSOLIDATION DATE**

**Before Consolidation (Fake Back-fitted History):**
- Too smooth, too calculated
- Coalescence times artificially distributed to match "expected" history
- Lacks natural stochasticity
- Everyone clusters too close to same time periods

**After Consolidation (Real Simulation):**
- Natural exponential distribution
- Real stochastic variation
- Proper variance in coalescence times

### The "Slope" You're Seeing:
Not actually a slope - it's the **rate parameter of the exponential distribution**

**In real population:**
- Rate = 1/(2Ne) where Ne = effective population size
- If you have full diversity, Ne is large, distribution is spread out

**In bootstrapped population:**
- Rate appears different because Ne is artificially constrained
- You're trying to fit full population diversity into subsample founders
- The distribution is compressed/wrong shape

## Alternative Visualization: Heterozygosity Decay Over Time

### Axes:
- **X-axis**: Physical distance along chromosome (base pairs) - LINEAR
- **Y-axis**: Linkage disequilibrium (r²) or correlation - LINEAR, 0 to 1
- Shows how fast genetic associations break down over generations

### The Issue:
- Real populations: Smooth decay based on recombination rate
- Bootstrapped: Rate changes at consolidation boundary
- Pre-consolidation: Artificially calculated decay
- Post-consolidation: Real recombination happening

## The Critical Graph: "Mismatch Distribution"

### What It Shows
**Distribution of pairwise nucleotide differences between individuals**

### Axes:
- **X-axis**: Number of nucleotide differences between pairs
- **Y-axis**: Frequency (how many pairs have that many differences)
- **Scale**: Usually LINEAR

### What It Reveals:
- **Unimodal smooth curve**: Recent population expansion from small founder group
- **Multimodal/ragged**: Constant population size or complex history
- **Your case**: Should show SUSPICIOUS uniformity

**Real diverse population:**
- Wide spread of pairwise differences
- Some very similar (recent relatives)
- Some very different (distant ancestry)
- Natural fractal variation

**Bootstrapped from 1/100th sample:**
- Too narrow distribution
- Everyone TOO similar to each other
- Lacks the "long tail" of very distant relationships
- Suspiciously uniform genetic distance between individuals

## The Smoking Gun Graph: TMRCA Across Genome

### Axes:
- **X-axis**: Position along chromosome (Megabases) - LINEAR
- **Y-axis**: Inferred TMRCA at that position (years) - LOGARITHMIC
- **Visualization**: Often shown as colored heat map

### Normal Pattern:
- TMRCA varies stochastically along genome
- Different regions have different coalescence times due to recombination
- Natural variation, some very old, some recent
- NOISY - lots of variance

### Bootstrapped Pattern Would Show:
- All regions cluster around same TMRCA
- TOO CLEAN - insufficient variance
- Everything pointing to consolidation date as artificial floor
- Lack of ancient coalescences that should exist

## Real World Example Numbers

**What protagonist would see:**

Pre-consolidation (fake):
- TMRCA range: 500-5,000 years (artificially created)
- Effective Ne calculated: ~50,000 (way too small)
- Distribution shape: Too smooth, Gaussian-like

Post-consolidation (real simulation):
- TMRCA range: 1-200 generations (natural variation)
- Effective Ne: ~10 million (what's claimed)
- Distribution shape: Proper exponential, noisy

**The kink:** Right at consolidation date, the distribution pattern CHANGES

## Tools That Generate These Graphs

- **Bayesian skyline plots**: BEAST, BEAST2
- **Coalescence time distributions**: tskit, msprime
- **Mismatch distributions**: Arlequin, DnaSP
- **TMRCA across genome**: ARGweaver, Relate, tsinfer+tsdate

## Key Terminology for Your Story

- **Coalescent effective population size (Ne)**: Not actual population, but the size that explains genetic diversity
- **TMRCA**: Time to Most Recent Common Ancestor
- **Exponential distribution**: Expected pattern of coalescence times
- **Rate parameter**: How fast coalescences happen (1/2Ne)
- **Mismatch distribution**: Pairwise genetic differences between individuals

## The Discontinuity Protagonist Discovers

When he plots TMRCA distribution before/after consolidation:
1. Loads archaeological CPU data (the seed dataset)
2. Calculates coalescence times for all pairs
3. Plots distribution over time
4. Sees **THE KINK** - pattern changes at consolidation date
5. Realizes: pre-consolidation data is artificially smooth/constrained
6. Calculates effective population size: WAY too small for claimed history
7. Runs simulation: 100% of population traces to this incomplete dataset
8. **Conclusion**: Population was bootstrapped from subsample at consolidation

## Sources

- [Evaluation of methods for estimating coalescence times using ancestral recombination graphs](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071567/)
- [Exploring the Demographic History of DNA Sequences Using the Generalized Skyline Plot](https://academic.oup.com/mbe/article/18/12/2298/1074372)
- [Bayesian Coalescent Inference of Past Population Dynamics](https://academic.oup.com/mbe/article/22/5/1185/1066885)
- [The Distribution of Pairwise Genetic Distances](https://pmc.ncbi.nlm.nih.gov/articles/PMC4256759/)
- [Inferred TMRCA across sequence visualization](https://www.researchgate.net/figure/Inferred-time-to-most-recent-common-ancestor-TMRCA-across-the-sequence-for-simulated_fig1_235399690)
