#!/usr/bin/env python3
"""
Generate coalescence time visualizations showing the difference between
real populations and bootstrapped simulations.

This demonstrates what the protagonist would see when analyzing genetic data.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

def generate_real_coalescence_times(n_pairs=1000, Ne=10000):
    """
    Generate realistic coalescence times following exponential distribution.

    Under coalescent theory: T ~ Exponential(1/(2*Ne))
    """
    rate = 1 / (2 * Ne)
    times = expon.rvs(scale=1/rate, size=n_pairs)
    return times

def generate_bootstrapped_coalescence_times(n_pairs=1000, Ne_real=10000, Ne_bootstrap=500):
    """
    Generate artificially constrained coalescence times from bootstrapped population.

    Bootstrapped from small sample - coalescence times cluster around recent time.
    """
    # Most coalescences happen very recently (small Ne from subsample)
    rate = 1 / (2 * Ne_bootstrap)
    times = expon.rvs(scale=1/rate, size=n_pairs)

    # Add artificial "smoothing" - too clean
    times = times + norm.rvs(0, rate/10, size=n_pairs)
    times = np.abs(times)  # No negative times

    return times

def plot_1_coalescence_distribution():
    """
    GRAPH 1: Pairwise Coalescence Time Distribution
    This is THE KEY GRAPH showing the discontinuity.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))

    # Real population
    real_times = generate_real_coalescence_times(n_pairs=5000, Ne=10000)
    ax1.hist(real_times, bins=100, density=True, alpha=0.7, color='steelblue', edgecolor='black')

    # Overlay theoretical exponential
    x = np.linspace(0, max(real_times), 1000)
    Ne = 10000
    theoretical = expon.pdf(x, scale=2*Ne)
    ax1.plot(x, theoretical, 'r--', linewidth=2, label='Theoretical Exponential')

    ax1.set_xlabel('Time to Most Recent Common Ancestor (generations)', fontsize=12)
    ax1.set_ylabel('Probability Density', fontsize=12)
    ax1.set_title('REAL POPULATION: Coalescence Time Distribution\n(Noisy, follows exponential distribution)', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Bootstrapped population (too smooth, wrong Ne)
    bootstrap_times = generate_bootstrapped_coalescence_times(n_pairs=5000, Ne_real=10000, Ne_bootstrap=500)
    ax2.hist(bootstrap_times, bins=100, density=True, alpha=0.7, color='salmon', edgecolor='black')

    # Overlay what it SHOULD be vs what it IS
    Ne_claimed = 10000
    Ne_actual = 500
    x2 = np.linspace(0, max(bootstrap_times)*2, 1000)
    should_be = expon.pdf(x2, scale=2*Ne_claimed)
    actually_is = expon.pdf(x2, scale=2*Ne_actual)

    ax2.plot(x2, should_be, 'b--', linewidth=2, label=f'Should be (Ne={Ne_claimed:,})', alpha=0.5)
    ax2.plot(x2, actually_is, 'r-', linewidth=2, label=f'Actually is (Ne={Ne_actual:,})')

    ax2.set_xlabel('Time to Most Recent Common Ancestor (generations)', fontsize=12)
    ax2.set_ylabel('Probability Density', fontsize=12)
    ax2.set_title('BOOTSTRAPPED POPULATION: Coalescence Time Distribution\n(Too constrained, reveals small effective population size)', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # THE KINK: Combined view showing discontinuity
    consolidation_time = 100  # generations ago

    # Before consolidation: artificial/smooth
    pre_consol = bootstrap_times
    # After consolidation: real exponential
    post_consol = generate_real_coalescence_times(n_pairs=5000, Ne=10000)
    post_consol = post_consol[post_consol < consolidation_time]  # Only recent times

    # Shift pre-consolidation times to be "in the past"
    pre_consol_shifted = pre_consol + consolidation_time

    # Combine and plot
    all_times = np.concatenate([post_consol, pre_consol_shifted])
    ax3.hist(all_times, bins=150, density=True, alpha=0.7, color='purple', edgecolor='black')

    # Mark the consolidation boundary
    ax3.axvline(consolidation_time, color='red', linestyle='--', linewidth=3,
                label=f'CONSOLIDATION DATE (kink at {consolidation_time} generations)')
    ax3.axvspan(0, consolidation_time, alpha=0.2, color='green', label='Real simulation (proper distribution)')
    ax3.axvspan(consolidation_time, max(all_times), alpha=0.2, color='orange', label='Fake back-fitted history (wrong distribution)')

    ax3.set_xlabel('Time to Most Recent Common Ancestor (generations)', fontsize=12)
    ax3.set_ylabel('Probability Density', fontsize=12)
    ax3.set_title('THE SMOKING GUN: Discontinuity at Consolidation Date\n(Pattern changes where fake history meets real simulation)', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('research/graph1_coalescence_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: graph1_coalescence_distribution.png")
    plt.close()

def plot_2_mismatch_distribution():
    """
    GRAPH 2: Mismatch Distribution (Pairwise Nucleotide Differences)
    Shows how uniform the genetic distances are (too uniform = bootstrapped)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Real population: wide spread of pairwise differences
    # Some very similar (siblings), some very different (distant ancestry)
    real_differences = np.concatenate([
        np.random.gamma(shape=2, scale=15, size=2000),  # Recent relatives
        np.random.gamma(shape=5, scale=30, size=3000),  # Distant relatives
    ])

    ax1.hist(real_differences, bins=80, density=True, alpha=0.7, color='steelblue', edgecolor='black')
    ax1.set_xlabel('Number of Nucleotide Differences', fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_title('REAL POPULATION: Mismatch Distribution\n(Wide spread, natural variation)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Bootstrapped: everyone TOO similar, suspiciously uniform
    bootstrap_differences = np.random.gamma(shape=8, scale=5, size=5000)

    ax2.hist(bootstrap_differences, bins=80, density=True, alpha=0.7, color='salmon', edgecolor='black')
    ax2.set_xlabel('Number of Nucleotide Differences', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.set_title('BOOTSTRAPPED POPULATION: Mismatch Distribution\n(Too narrow, suspiciously uniform - everyone too similar)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # Add statistics
    ax1.text(0.7, 0.9, f'Mean: {real_differences.mean():.1f}\nStd: {real_differences.std():.1f}',
             transform=ax1.transAxes, fontsize=11, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax2.text(0.7, 0.9, f'Mean: {bootstrap_differences.mean():.1f}\nStd: {bootstrap_differences.std():.1f}',
             transform=ax2.transAxes, fontsize=11, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig('research/graph2_mismatch_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: graph2_mismatch_distribution.png")
    plt.close()

def plot_3_bayesian_skyline():
    """
    GRAPH 3: Bayesian Skyline Plot
    Shows effective population size over time (LOGARITHMIC scales)
    """
    fig, ax = plt.subplots(figsize=(14, 8))

    # Time points (years before present) - LOGARITHMIC
    time = np.logspace(2, 5, 100)  # 100 to 100,000 years ago

    # Real population: natural growth and bottlenecks
    Ne_real = 10000 * np.exp(time / 30000)  # Exponential growth
    # Add some bottleneck events
    Ne_real[time > 50000] *= 0.3  # Ancient bottleneck
    Ne_real[time < 1000] *= 1.5   # Recent expansion

    # Bootstrapped simulation population
    consolidation_date = 500  # years ago
    Ne_bootstrap = np.copy(Ne_real)

    # Before consolidation: artificial, too smooth, wrong size
    mask_before = time > consolidation_date
    Ne_bootstrap[mask_before] = 5000 * (1 + 0.1 * np.log(time[mask_before]))  # Too flat

    # After consolidation: matches real (because simulation is running)
    mask_after = time <= consolidation_date
    Ne_bootstrap[mask_after] = Ne_real[mask_after]

    # Plot on LOG-LOG scale
    ax.plot(time, Ne_real, 'b-', linewidth=2, label='Real Population History', alpha=0.7)
    ax.plot(time, Ne_bootstrap, 'r-', linewidth=2, label='Bootstrapped Simulation', alpha=0.7)

    # Mark consolidation
    ax.axvline(consolidation_date, color='green', linestyle='--', linewidth=3,
               label=f'Consolidation Date ({consolidation_date} years ago)')

    # Shade confidence intervals (would be calculated from data)
    ax.fill_between(time, Ne_real * 0.7, Ne_real * 1.3, alpha=0.2, color='blue')
    ax.fill_between(time, Ne_bootstrap * 0.7, Ne_bootstrap * 1.3, alpha=0.2, color='red')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Time Before Present (years) - LOG SCALE', fontsize=12)
    ax.set_ylabel('Effective Population Size (Ne) - LOG SCALE', fontsize=12)
    ax.set_title('Bayesian Skyline Plot: Population Size Over Time\n(Notice the discontinuity at consolidation)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('research/graph3_bayesian_skyline.png', dpi=300, bbox_inches='tight')
    print("Saved: graph3_bayesian_skyline.png")
    plt.close()

def plot_4_tmrca_across_genome():
    """
    GRAPH 4: TMRCA Across Genome Position
    Shows how TMRCA varies along chromosome (should be noisy, not smooth)
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))

    # Genome positions (Megabases)
    positions = np.linspace(0, 100, 1000)  # 100 Mb chromosome

    # Real population: NOISY variation in TMRCA along genome
    tmrca_real = 10000 + 5000 * np.sin(positions / 10) + np.random.normal(0, 2000, size=len(positions))
    tmrca_real = np.abs(tmrca_real)  # No negative times

    ax1.plot(positions, tmrca_real, linewidth=0.5, color='steelblue', alpha=0.7)
    ax1.fill_between(positions, tmrca_real, alpha=0.3, color='steelblue')
    ax1.set_xlabel('Position Along Chromosome (Megabases)', fontsize=12)
    ax1.set_ylabel('TMRCA (generations) - LOG SCALE', fontsize=12)
    ax1.set_yscale('log')
    ax1.set_title('REAL POPULATION: TMRCA Across Genome\n(Noisy, natural variation from recombination)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Bootstrapped: TOO SMOOTH, everything clusters around same time
    tmrca_bootstrap = 1000 + 200 * np.sin(positions / 10) + np.random.normal(0, 50, size=len(positions))
    tmrca_bootstrap = np.abs(tmrca_bootstrap)

    ax2.plot(positions, tmrca_bootstrap, linewidth=0.5, color='salmon', alpha=0.7)
    ax2.fill_between(positions, tmrca_bootstrap, alpha=0.3, color='salmon')
    ax2.axhline(1000, color='red', linestyle='--', linewidth=2,
                label='Artificial floor at consolidation date')
    ax2.set_xlabel('Position Along Chromosome (Megabases)', fontsize=12)
    ax2.set_ylabel('TMRCA (generations) - LOG SCALE', fontsize=12)
    ax2.set_yscale('log')
    ax2.set_title('BOOTSTRAPPED POPULATION: TMRCA Across Genome\n(Too smooth, too uniform - lacks ancient coalescences)', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('research/graph4_tmrca_across_genome.png', dpi=300, bbox_inches='tight')
    print("Saved: graph4_tmrca_across_genome.png")
    plt.close()

def plot_5_the_smoking_gun():
    """
    GRAPH 5: The Combined Evidence
    What protagonist sees that proves it's a simulation
    """
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Top: The kink in coalescence times
    ax1 = fig.add_subplot(gs[0, :])

    consolidation_time = 100
    pre_consol = generate_bootstrapped_coalescence_times(n_pairs=3000, Ne_real=10000, Ne_bootstrap=500)
    post_consol = generate_real_coalescence_times(n_pairs=3000, Ne=10000)
    post_consol = post_consol[post_consol < consolidation_time]
    pre_consol_shifted = pre_consol + consolidation_time
    all_times = np.concatenate([post_consol, pre_consol_shifted])

    ax1.hist(all_times, bins=150, density=True, alpha=0.7, color='purple', edgecolor='black')
    ax1.axvline(consolidation_time, color='red', linestyle='--', linewidth=4)
    ax1.axvspan(0, consolidation_time, alpha=0.2, color='green')
    ax1.axvspan(consolidation_time, max(all_times), alpha=0.2, color='orange')
    ax1.set_xlabel('Time to MRCA (generations)', fontsize=11)
    ax1.set_ylabel('Density', fontsize=11)
    ax1.set_title('1. THE KINK: Coalescence pattern changes at consolidation', fontsize=13, fontweight='bold')
    ax1.text(consolidation_time + 50, ax1.get_ylim()[1]*0.8,
             'DISCONTINUITY\nHERE!', fontsize=14, color='red', fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # Middle left: Effective population size too small
    ax2 = fig.add_subplot(gs[1, 0])

    categories = ['Claimed\nPopulation', 'Actual Genetic\nDiversity Implies']
    Ne_values = [10000000, 50000]
    colors = ['green', 'red']

    bars = ax2.bar(categories, Ne_values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Effective Population Size (Ne)', fontsize=11)
    ax2.set_yscale('log')
    ax2.set_title('2. IMPOSSIBLE Ne: Claimed vs Actual', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    for bar, val in zip(bars, Ne_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height*1.2,
                f'{val:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Middle right: 100% trace to subsample
    ax3 = fig.add_subplot(gs[1, 1])

    # Pie chart showing everyone descends from subsample
    sizes = [100]
    labels = ['100% of population\ntraces to subsample\nat consolidation date']
    colors_pie = ['#ff6b6b']
    explode = [0.1]

    ax3.pie(sizes, explode=explode, labels=labels, colors=colors_pie, autopct='%1.0f%%',
            shadow=True, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax3.set_title('3. IMPOSSIBLE ANCESTRY: No diversity before subsample', fontsize=13, fontweight='bold')

    # Bottom: Time to subsample
    ax4 = fig.add_subplot(gs[2, :])

    # Simulate what percentage of population traces back at different times
    generations_back = np.arange(0, 300)

    # Real population: everyone eventually traces back, but gradually
    real_trace = 100 * (1 - np.exp(-generations_back / 50))

    # Bootstrapped: EVERYONE traces back exactly at consolidation
    bootstrap_trace = np.zeros_like(generations_back, dtype=float)
    bootstrap_trace[generations_back >= consolidation_time] = 100.0

    ax4.plot(generations_back, real_trace, 'b-', linewidth=2, label='Expected (Real Population)', alpha=0.7)
    ax4.plot(generations_back, bootstrap_trace, 'r-', linewidth=3, label='Observed (Simulation)', alpha=0.7)
    ax4.axvline(consolidation_time, color='green', linestyle='--', linewidth=2, alpha=0.5)
    ax4.fill_between(generations_back, bootstrap_trace, alpha=0.3, color='red')

    ax4.set_xlabel('Generations Back in Time', fontsize=11)
    ax4.set_ylabel('% of Population Tracing to Common Ancestor', fontsize=11)
    ax4.set_title('4. THE PROOF: Everyone traces to same date (impossible without bootstrap)', fontsize=13, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim([0, 105])

    # Add overall title
    fig.suptitle('THE SMOKING GUN: Combined Evidence of Bootstrapped Simulation',
                 fontsize=16, fontweight='bold', y=0.995)

    plt.savefig('research/graph5_smoking_gun.png', dpi=300, bbox_inches='tight')
    print("Saved: graph5_smoking_gun.png")
    plt.close()

if __name__ == "__main__":
    print("Generating coalescence time visualizations...")
    print("=" * 60)

    print("\nGenerating Graph 1: Coalescence Time Distribution...")
    plot_1_coalescence_distribution()

    print("\nGenerating Graph 2: Mismatch Distribution...")
    plot_2_mismatch_distribution()

    print("\nGenerating Graph 3: Bayesian Skyline Plot...")
    plot_3_bayesian_skyline()

    print("\nGenerating Graph 4: TMRCA Across Genome...")
    plot_4_tmrca_across_genome()

    print("\nGenerating Graph 5: The Smoking Gun...")
    plot_5_the_smoking_gun()

    print("\n" + "=" * 60)
    print("All graphs generated successfully!")
    print("Check the research/ folder for PNG files.")
