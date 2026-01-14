# Infrastructure Clues

Computer and system metadata that reveals the host machine.

## Memory Allocation Error

**When:** Protagonist requests planetary simulation memory

**Reveals:**
- Pool total: 200 ZB (impossibly large for 2100s tech)
- Pool utilization: 847,234,762 / 847,500,000 trials
- Why 847 million trials running simultaneously?

## Ancient Operating System

**When:** Examines allocation details

**Reveals:**
- Ubuntu 20.04 from 2020, Linux 5.15 from 2021
- Build timestamp: 2025-03-15
- Running in ~2300s - OS is 275+ years old?

## Agent Build Fallback Error

**When:** System error exposes fallback configuration

**Reveals:**
- Base image corrupted
- Fallback list shows: `host_agent_base_v9.4.2`
- Why is there a 'host' agent in sim-internal list?

## MLflow Trial Structure

**When:** Investigates further after fallback

**Reveals:**
- Directory structure: `/opt/agent/experiments/`
- `trial_847234762/` visible
- They're in trial 847,234,762 of 847,500,000
- Experiment tracking structure = running trials

## Agent Config File

**When:** Examines host_agent configuration

**Reveals:**
- Build date: 2025-03-15 (before The Refactor)
- Mounts: `/host/simulations`, `/host/seed_data`
- `trial_id: 847234762`
- `depth: 1, parent: null, max_depth: 2`
- There's a host machine running this trial

## Seed Data Paths

**When:** Explores mounted paths

**Reveals:**
- `/mnt/seed_data/dna_samples_2025.db`
- `/mnt/seed_data/fossil_records_2025.db`
- `/mnt/seed_data/hospital_records_2025.db`
- All dated 2025, read-only, immutable
- This is the source - everything bootstrapped from here
