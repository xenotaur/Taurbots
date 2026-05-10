---
id: external-simulator-and-benchmark-adapters
title: External Simulator and Benchmark Adapters
status: active
owner: maintainers
---

# External Simulator and Benchmark Adapters

## Purpose

Treat BARN, ArenaBench, ROS 2/Gazebo, Webots, MuJoCo, and related systems as external validation backends. Taurbots should provide repeatable adapter contracts, recipes, wrappers, and result normalization without allowing benchmark assumptions to define core internals.

## Scope

- Adapter contract sketch: prepare, build, run_episode, run_batch, collect_results, and normalize_results.
- BARN ROS 2 as a likely first modern benchmark target.
- ArenaBench container path as a likely legacy/ROS 1-era target.
- Webots versus MuJoCo as an open question for the first non-`simple2d` simulator adapter.
- Benchmark recipes as generated scripts/docs before full automation.
- Normalized result records that compare Taurbots-native runs with external-backend runs.

## Non-Goals

- Do not vendor external benchmark repositories or simulator binaries.
- Do not make BARN, ArenaBench, ROS 2/Gazebo, Webots, or MuJoCo required for core tests.
- Do not build full benchmark automation before the adapter contract and result schema are stable.

## First Milestones

1. Define the benchmark adapter contract and lifecycle verbs.
2. Create a BARN ROS 2 recipe plan.
3. Create an ArenaBench container recipe plan.
4. Evaluate Webots versus MuJoCo as the first non-`simple2d` simulator adapter.
5. Design normalized benchmark result import/export.

## Initial Work Items

- `project/work_items/WI-TAURBOTS-BENCHMARK-ADAPTERS-RECIPES.md`

## Relationship to Adopted Design

This workstream implements the adopted design's adapters-are-replaceable and benchmarks-are-validation-backends principles. It depends on stable core concepts and result records, but should not pull external benchmark assumptions into the core.
