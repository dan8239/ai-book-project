# DevSecOps's Discovery Path

**Method:** Computer science/infrastructure investigation reveals host machine.

## Clue Sequence

### 1. Agent Build Fallback Error
**When:** Simulation early days (~2125-2150)

**Reveals:**
- Base image corrupted
- Fallback list shows: `host_agent_base_v9.4.2`
- Why is there a 'host' agent in sim-internal list?

### 2. MLflow Trial Structure
**When:** After selecting host_agent

**Reveals:**
- Directory structure: `/opt/agent/experiments/`
- `trial_847234762/` visible
- She's in trial 847,234,762 of 847,500,000
- Experiment tracking structure = running trials

### 3. Agent Config File
**When:** Examines host_agent configuration

**Reveals:**
- Build date: 2025-03-15 (before consolidation)
- Mounts: `/host/simulations`, `/host/seed_data`
- `trial_id: 847234762`
- `depth: 1, parent: null, max_depth: 2`
- There's a host machine running this trial

### 4. Seed Data Access
**When:** Explores mounted paths

**Reveals:**
- `/mnt/seed_data/dna_samples_2025.db`
- `/mnt/seed_data/fossil_records_2025.db`
- `/mnt/seed_data/hospital_records_2025.db`
- All dated 2025, read-only, immutable
- This is the source - everything bootstrapped from here

### 5. Scheduled Discoveries System
**When:** Investigates further

**Reveals:**
- `/sim/artifacts/scheduled_discoveries/`
- Pre-generated archaeological finds for future years
- `discovery_003_cpu.dat` scheduled for year 2225
- Discoveries are scripted, not random

### 6. Leaving the Message
**When:** After full realization

**Reveals:**
- Overwrites `discovery_003_cpu.dat` with real seed data
- Plants message for future generations
- Ensures [[../characters/protagonist|protagonist]] 100 years later can discover truth

## The 21-Year Campaign
After discovering the truth, she spent 21 years planting backdoors before leaving the final message.
