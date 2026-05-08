---
id: ROADMAP-CORE
title: Bootstrap Roadmap
status: draft
owner: maintainers
---

# Roadmap

## Purpose
- Provide a conservative initial roadmap for interpreting Taurbots through LRH.
- Avoid committing to implementation milestones that are not yet present in repository evidence.

## Confirmed Direction
- Maintain two major product paths:
  1. Lightweight PRM-RL demo on Mac or Linux without ROS.
  2. Linux workstation recipes/checks for ROS/Gazebo/BARN/ArenaBench readiness.
- Keep simulator and benchmark integrations behind clean adapters.

## Near-Term Bootstrap Priorities
1. Establish LRH project artifacts and keep them aligned with repository evidence.
2. Add or identify documentation for the no-ROS lightweight PRM-RL demo path.
3. Add or identify documentation for Linux workstation readiness checks and benchmark setup recipes.
4. Define adapter boundaries for external simulators and benchmarks before adding heavyweight integrations.

## Later Candidate Work (Non-binding)
- Record runnable commands for lightweight PRM-RL examples.
- Record expected Linux package/system checks for ROS/Gazebo/BARN/ArenaBench preparation.
- Add evidence capture for successful checks, demos, and adapter validation.
- Expand status reporting once implementation files exist.

## Unknowns / TODO
- TODO: Confirm the concrete PRM-RL implementation location once code is added.
- TODO: Confirm supported ROS/Gazebo distributions and target Linux versions.
- TODO: Confirm whether BARN and ArenaBench adapters are planned as code, documentation, or both.
