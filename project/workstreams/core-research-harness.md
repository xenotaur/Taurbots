---
id: core-research-harness
title: Core Research Harness
status: active
owner: maintainers
---

# Core Research Harness

## Purpose

Establish the simulator-independent Taurbots core for robot-navigation research: portable concepts, structured experiment records, a lightweight Mac/Linux research loop, and PRM-RL as the first algorithm module without making PRM-RL the whole product identity.

## Scope

- Core concepts including State/Pose/Observation/Action, World/Map/Scenario, RobotModel, Task, Policy/PolicyRunner, SimulatorBackend, RolloutEngine, Roadmap, EdgeEvaluator, Planner, Episode, EvaluationRecord, and ExperimentProfile.
- A unit-testable, non-ROS core package boundary.
- A simple `simple2d` simulator path for Mac/Linux smoke tests.
- A PRM-RL module as the first algorithm implementation.
- Initial structured result records, likely JSONL unless a later design chooses otherwise.
- Policy, roadmap, profile, and result serialization strategy.

## Non-Goals

- Do not require ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, or GPU tooling for core tests.
- Do not bind core APIs to Gymnasium, Stable-Baselines3, NetworkX, Shapely, or any one RL/graph framework.
- Do not present PRM-RL as the entire Taurbots product boundary.

## First Milestones

1. Define package layout, CLI entry-point direction, docs/test conventions, and safe default dependencies.
2. Specify core abstractions and experiment/result schema.
3. Plan the `simple2d` smoke-test environment.
4. Specify PRM-RL module interfaces and baseline workflow.
5. Specify serialization for policies, roadmaps, experiment profiles, and result records.

## Initial Work Items

- `project/work_items/WI-TAURBOTS-CORE-SKELETON.md`
- `project/work_items/WI-TAURBOTS-CORE-ABSTRACTIONS-SCHEMA.md`
- `project/work_items/WI-TAURBOTS-SIMPLE2D-PRMRL-SMOKE.md`

## Relationship to Adopted Design

This workstream implements the adopted design's core-before-adapters principle and preserves the lightweight Mac/Linux local research loop. It should remain independent of external benchmark and simulator assumptions documented in the workstation and adapter workstreams.
