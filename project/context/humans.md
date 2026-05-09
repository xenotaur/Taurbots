# Project Context (Human-Oriented)

## One-line Description
- Taurbots is intended to be a reproducible robot-navigation research harness for lightweight PRM-RL demos and Linux benchmark-environment preparation.

## Overview
- The repository README identifies Taurbots as supporting clean starts for robot navigation and embodied-AI experiments.
- The requested project direction describes two major paths:
  - a lightweight PRM-RL demo that runs on Mac or Linux without ROS;
  - Linux workstation recipes/checks for serious ROS/Gazebo/BARN/ArenaBench preparation.
- The LRH `project/` directory is a control plane for interpreting goals, focus, guardrails, evidence, status, and decisions.

## Goals and Direction
- Goal: provide a reproducible robot-navigation research harness for researchers and developers working with lightweight PRM-RL experiments and heavier Linux benchmark environments.
- Near-term focus: establish the LRH control plane, preserve explicit uncertainty, and prepare for evidence-backed demo/check/adapter work.

## Design Snapshot
- Authoritative intent lives in `principles/`, `goal/`, `roadmap/`, and `design/`.
- Execution planning lives in `focus/`, `work_items/`, and `contributors/`.
- Safety, approval, cost, and optics constraints live in `guardrails/`.
- Evidence-backed truth and audit history live in `evidence/`, `status/`, and `memory/`.
- Conceptually, Taurbots should keep lightweight no-ROS experiments separate from heavyweight Linux benchmark preparation and external simulator/benchmark adapters.

## Current Status Snapshot
- Health: yellow.
- The project identity and direction are coherent, but implementation evidence is sparse at bootstrap time.
- No source modules, tests, recipes, or adapters were observed during the initial inspection, so runnable capabilities remain unverified until future evidence is added.

## Known Unknowns
- Exact location and command for the lightweight PRM-RL demo.
- Supported Mac/Linux versions and runtime dependencies.
- Supported ROS/Gazebo distributions and Linux setup targets.
- Whether BARN and ArenaBench support will be provided as recipes, adapters, documentation, or a combination.
- Named maintainers or owners for project areas.

## Notes
- Derived summary only (non-authoritative).
- If this file conflicts with authoritative artifacts, prefer `principles/`, `goal/`, `roadmap/`, `design/`, `focus/`, `guardrails/`, `evidence/`, `status/`, and `memory/`.
