# Simulation Architecture

## Scale
- **Total trials:** 847+ million running simultaneously
- **Success rate:** 0.04% reach stability threshold
- **Median extinction:** 127 years

## Time Mechanics
- **Time dilation ratio:** ~111,500:1
- 10 sim minutes = 5 milliseconds host time
- Entire civilization runs in minutes on host machine

## Technical Details (Clues)

### Memory Allocation
- Pool total: 200 ZB (impossibly large for 2100s tech)
- Pool utilization: 847,234,762 / 847,500,000 trials
- Why 847 million trials running simultaneously?

### Operating System
- Ubuntu 20.04 from 2020, Linux 5.15 from 2021
- Build timestamp: 2025-03-15
- Running in ~2300s - OS is 275+ years old?

### Trial Structure
- Directory structure: `/opt/agent/experiments/`
- Each trial has ID (e.g., trial_847234762/)
- MLflow-style experiment tracking structure

### Agent Configuration
- Build date: 2025-03-15 (before The Refactor)
- Mounts: `/host/simulations`, `/host/seed_data`
- `depth: 1, parent: null, max_depth: 2`
- There's a host machine running this trial

## Seed Data
Located at `/mnt/seed_data/`:
- `dna_samples_2025.db`
- `fossil_records_2025.db`
- `hospital_records_2025.db`

All dated 2025, read-only, immutable. This is the source - everything bootstrapped from here.

## Damon's Neural Network Study / Surveillance Depth

The reason Damon and team are using it is actually that studying the simplified brain neural network — just understanding how every neuron works, and these agents, and what correlates to what on a simplified simulation — lets us study our own brains at a lower granularity. That's why Damon is doing it. He can do whatever because he's got an agent army under him.

More on the neural studying — it's to the point where they know the bowel movements of every human. When they go. They know the pupil dilation. They know blood pressure. Whatever. And it's all from mapping the brain activity extensively. They just know what everything is doing. You can opt out of seeing the information yourself but you can't opt out of them collecting the data. For every human, ever. They know if your eyes are dilated, they know what you ate, they know if you exercise, heart rate — anything in medicine would use.

## Scheduled Discoveries
Located at `/sim/artifacts/scheduled_discoveries/`:
- Pre-generated archaeological finds for future years
- `discovery_003_cpu.dat` scheduled for year 2125
- Discoveries are scripted, not random
