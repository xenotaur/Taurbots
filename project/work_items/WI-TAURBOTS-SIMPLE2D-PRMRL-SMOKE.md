---
id: WI-TAURBOTS-SIMPLE2D-PRMRL-SMOKE
title: Simple2d PRM-RL smoke-test environment
status: proposed
priority: high
owner: maintainers
workstream: core-research-harness
---

# WI-TAURBOTS-SIMPLE2D-PRMRL-SMOKE: Simple2d PRM-RL Smoke-Test Environment

## Objective

Plan and later implement the first lightweight Mac/Linux environment for local Taurbots research iteration, using `simple2d` and a PRM-RL baseline path without requiring ROS or heavyweight simulator stacks.

## Scope

- Define the `simple2d` environment assumptions, map/scenario format, robot model limits, task definitions, and deterministic smoke-test cases.
- Define how PRM-RL plugs into core planner, roadmap, edge evaluator, and policy runner interfaces.
- Specify minimum tests for deterministic rollouts, schema-compatible result output, and reproducible seeds.
- Document how this environment remains a smoke-test path rather than a scientific benchmark substitute.

## Non-Goals

- Do not claim performance parity with external benchmarks.
- Do not require ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, GPU drivers, or workstation setup.
- Do not make PRM-RL the only supported future algorithm family.

## Acceptance Criteria

- A future implementation PR can add `simple2d` and PRM-RL baseline pieces incrementally.
- The plan references core abstractions and result schema rather than defining incompatible local-only types.
- Smoke tests remain small enough for routine local or CI execution.

## Related Workstream

- `project/workstreams/core-research-harness.md`
