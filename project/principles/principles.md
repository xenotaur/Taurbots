---
id: PRINCIPLES-CORE
title: Taurbots Operating Principles
status: active
owner: maintainers
time_horizon: long
---

# Principles

## Reproducibility First
- Prefer documented, repeatable commands, checks, recipes, and environment assumptions over implicit local setup.
- Treat benchmark preparation and experiment execution as auditable workflows whose inputs and outputs can be inspected.

## Lightweight Before Heavyweight
- Preserve a path for Mac/Linux PRM-RL experimentation that does not require ROS, Gazebo, BARN, or ArenaBench.
- Keep heavyweight simulator and benchmark integration behind clean adapters and Linux preparation recipes.

## Research Harness, Not Monolith
- Separate lightweight demos, workstation readiness checks, and external simulator/benchmark bridges.
- Favor modular adapters and recipes that researchers can validate independently.

## Safety and Non-Destructive Automation
- Setup checks and recipes should default to read-only or clearly reversible behavior unless a user explicitly opts into changes.
- Avoid commands that unexpectedly alter robot, simulator, operating-system, or network state.

## Evidence-Backed Status
- Project status claims should cite repository files, commands, or generated evidence.
- Unknowns should remain explicit TODOs until validated by implementation or maintainer confirmation.
