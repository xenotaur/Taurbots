---
id: WI-TAURBOTS-BENCHMARK-ADAPTERS-RECIPES
title: Benchmark adapter contract and first recipes
status: proposed
priority: medium
owner: maintainers
workstream: external-simulator-and-benchmark-adapters
---

# WI-TAURBOTS-BENCHMARK-ADAPTERS-RECIPES: Benchmark Adapter Contract and First Recipes

## Objective

Define the first external benchmark adapter contract and recipe plans so Taurbots can later validate native experiments against BARN, ArenaBench, ROS 2/Gazebo, Webots, MuJoCo, and related systems without coupling core APIs to those stacks.

## Scope

- Define adapter lifecycle verbs: prepare, build, run_episode, run_batch, collect_results, and normalize_results.
- Plan a BARN ROS 2 recipe as the first likely modern benchmark target.
- Plan an ArenaBench container recipe as the first likely legacy/ROS 1-era benchmark path.
- Capture the Webots-versus-MuJoCo decision as a design spike for the first non-`simple2d` simulator adapter.
- Define normalized benchmark result import/export expectations compatible with core EvaluationRecord and ExperimentProfile concepts.

## Non-Goals

- Do not vendor benchmark repositories or simulator assets.
- Do not install ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, or cloud tooling.
- Do not implement full benchmark automation before recipes and result schemas are reviewed.

## Acceptance Criteria

- Adapter contract is documented clearly enough for future code or recipe PRs.
- BARN ROS 2 and ArenaBench recipe plans identify host/container boundaries and expected outputs.
- Normalized result records can compare Taurbots-native and external-backend runs.

## Related Workstream

- `project/workstreams/external-simulator-and-benchmark-adapters.md`
