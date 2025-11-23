# Statistical Genetics 101

## What is Statistical Genetics?

Statistical genetics is the field that applies statistical methods to genetic data to understand how genes influence traits and diseases. The goal is to find patterns in massive genetic datasets - typically screening hundreds of thousands to millions of genetic variants across large populations to identify which variants are associated with specific traits or health outcomes.

## What Do Statistical Geneticists Actually Do?

### Day-to-Day Work

Statistical geneticists spend most of their time:

**Data Quality Control:**
- Filtering out unreliable genetic markers (SNPs - single nucleotide polymorphisms)
- Checking for sample mix-ups, relatedness between individuals, ethnic outliers
- Validating that data follows expected patterns (Hardy-Weinberg equilibrium)
- Removing variants with low frequency or high missingness

**Running Analyses:**
- Testing associations between genetic variants and traits
- Using specialized genetics software (PLINK, IMPUTE2, Minimac, Beagle, MaCH)
- Performing statistical tests across entire genomes (genome-wide association studies/GWAS)
- Calculating heritability, genetic correlations, and risk predictions

**Interpreting Biological Meaning:**
- Once candidate regions are found, identifying the actual causative variant
- Exploring functional consequences of identified variants
- Translating statistical signals into biological insights about disease mechanisms
- Connecting genetic findings to clinical applications and drug development

### The Core Question They Ask

"What does this genetic signal tell us?"

They're looking at population-level patterns: linkage disequilibrium, selection signatures, demographic history, population bottlenecks. They interpret what the DNA variation *means* - whether it's a disease risk factor, an evolutionary adaptation, or an artifact of population history.

## What Their Research Projects Look Like

### Genome-Wide Association Studies (GWAS)

The bread-and-butter of statistical genetics. A typical GWAS project:

1. Collect genetic data from thousands to millions of individuals
2. Measure a trait or disease outcome across all those people
3. Test each genetic variant to see if it's associated with the trait
4. Apply rigorous statistical corrections for multiple testing
5. Identify variants that survive correction and replicate in independent datasets
6. Figure out what those variants actually *do* biologically

### Population Genetics Projects

Understanding human evolutionary history and demographic patterns:

- Tracing migrations and admixture between populations
- Detecting signatures of natural selection
- Estimating effective population sizes and bottleneck events
- Reconstructing ancestral relationships

### Clinical Risk Prediction

Building polygenic risk scores - combining many small genetic effects to predict disease risk or drug response in individuals.

## The Statistical Challenge

The core challenge is massive multiple testing: when you test millions of variants, many will look significant by chance. Statistical geneticists need rigorous methods to separate true signals from noise, which requires:

- Sophisticated statistical corrections
- Large sample sizes for adequate statistical power
- Replication in independent cohorts
- Biological validation of findings

## Key Concepts

**SNPs (Single Nucleotide Polymorphisms):** Single-letter variations in DNA sequence that are tested for associations.

**Hardy-Weinberg Equilibrium:** Expected genotype frequencies in a population - deviations suggest problems with data quality or interesting biology.

**Minor Allele Frequency (MAF):** How common the less-frequent version of a variant is - rare variants need special statistical treatment.

**Linkage Disequilibrium:** When nearby genetic variants are inherited together, complicating which variant is actually causal.

**Population Stratification:** Genetic differences between ancestry groups that can create spurious associations if not properly controlled.

## Sources

- [Genome-wide association study - Wikipedia](https://en.wikipedia.org/wiki/Genome-wide_association_study)
- [Genome-wide association studies | Nature Reviews Methods Primers](https://www.nature.com/articles/s43586-021-00056-9)
- [10 Years of GWAS Discovery: Biology, Function, and Translation](https://pmc.ncbi.nlm.nih.gov/articles/PMC5501872/)
- [A tutorial on conducting genome‐wide association studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC6001694/)
