---
id: WI-TAURBOTS-CORE-SKELETON
title: Core package skeleton and project conventions
status: completed
priority: high
owner: maintainers
workstream: core-research-harness
---

# WI-TAURBOTS-CORE-SKELETON: Core Package Skeleton and Project Conventions

## Objective

Establish the first implementation scaffold for Taurbots without adding runtime-heavy simulator, benchmark, ROS/Gazebo, or RL-framework dependencies.

## Scope

- Define package layout for core types, algorithm modules, adapters, CLI entry points, docs, tests, and examples.
- Identify the intended CLI entry-point direction, including eventual `taurbots doctor` placement without implementing full workstation diagnostics in this item.
- Choose conservative default dependency rules for the first implementation PR.
- Document tests/docs conventions for future core, simple2d, workstation, and adapter work.
- Keep the skeleton compatible with Mac/Linux local development.

## Non-Goals

- Do not implement PRM-RL behavior, simulators, benchmark recipes, or workstation mutation commands in this item.
- Do not add heavyweight dependencies such as ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Stable-Baselines3, Gymnasium, NetworkX, or Shapely.

## Acceptance Criteria

- A small package skeleton exists and is documented.
- The skeleton makes core/adapters separation visible.
- Lightweight validation commands are documented and runnable in the repository environment.
- The implementation does not require external simulator or benchmark installations.

## Related Workstream

- `project/workstreams/core-research-harness.md`

## Completion Note

Completed by the core skeleton and initial CI PR for prompt
`PROMPT(AD_HOC:taurbots-core-skeleton-ci)[20260511T000000Z]`. The completed
scope adds the minimal `src/taurbots` package, CLI placeholders, packaging
metadata, unittest-based smoke tests, lightweight developer scripts, and initial
GitHub Actions workflows while leaving algorithms, simulators, benchmark
adapters, and workstation diagnostics for later work items.
