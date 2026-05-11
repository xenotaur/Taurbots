---
id: ROADMAP-CORE
title: Taurbots Planning Roadmap
status: active
owner: maintainers
---

# Roadmap

## Purpose

Provide a staged, lightweight roadmap for turning the adopted Taurbots research-harness design into implementation PRs. This roadmap is intentionally high-level: it names sequencing, boundaries, and validation direction without solving every package or simulator detail in advance.

## Adopted Direction

Taurbots is a simulator-agnostic robot-navigation research harness with three primary planning workstreams:

1. **Core research harness**: simulator-independent abstractions, structured experiment records, a lightweight Mac/Linux local loop, and PRM-RL as the first algorithm module.
2. **Kubuntu benchmark workstation**: diagnostic-first setup guidance for Linux/NVIDIA workstations that run heavier simulator, GPU, ROS/Gazebo, and benchmark workloads.
3. **External simulator and benchmark adapters**: adapter contracts and recipes that keep BARN, ArenaBench, ROS 2/Gazebo, Webots, MuJoCo, and similar systems outside the core.

The adopted design proposal remains the durable architecture source for these boundaries: `project/design/proposals/adopted/taurbots-research-harness-and-benchmark-workstation.md`.

## Staged Sequence

1. **Planning/control-plane alignment**: keep roadmap, current focus, workstreams, and initial work items aligned with the adopted design.
2. **Kubuntu workstation diagnostics and setup docs**: document and later implement `taurbots doctor`-style checks for SSH/byobu/screen workflow, GPU readiness, Docker/NVIDIA Container Toolkit, optional Apptainer/Singularity, and ROS/Gazebo readiness before mutating setup automation.
3. **Core package skeleton and safe default tooling**: define package layout, CLI entry-point direction, docs/test conventions, and conservative dependency posture without adding heavyweight simulator stacks.
4. **Core abstractions and experiment schema**: specify simulator-independent concepts such as State/Pose/Observation/Action, World/Map/Scenario, RobotModel, Task, Policy/PolicyRunner, SimulatorBackend, RolloutEngine, Roadmap, EdgeEvaluator, Planner, Episode, EvaluationRecord, and ExperimentProfile.
5. **Simple2d environment and smoke tests**: create the lightweight Mac/Linux no-ROS path for fast local iteration and CI-friendly smoke checks.
6. **PRM-RL first algorithm module**: add PRM-RL as the first algorithm implementation while keeping Taurbots identity broader than PRM-RL.
7. **BARN ROS 2 and ArenaBench recipe/adapters**: sketch repeatable recipes and adapter wrappers for a modern ROS 2 benchmark target and a likely legacy/containerized benchmark target.
8. **Optional Webots/MuJoCo adapter**: evaluate Webots versus MuJoCo as the first non-`simple2d` simulator adapter through a design spike before implementation.
9. **ROS 2/Gazebo integration and benchmark validation**: connect stable core results to external validation backends with normalized result import/export.
10. **Deferred MCP/agentic wrappers**: consider agentic or MCP surfaces only after commands are stable, auditable, and have explicit safety boundaries.

This ordering intentionally matches the adopted design proposal's initial implementation path by putting diagnostic-first workstation documentation ahead of mutating setup automation and before deeper benchmark work. Core skeleton and schema work may still proceed in parallel, but the roadmap should not imply that workstation readiness is an afterthought.

## Near-Term Priority

The next implementation PRs should prefer the first four stages: planning alignment, diagnostic-first workstation documentation, core skeleton conventions, and core abstractions/result schema. Workstation diagnostics and core work can proceed in parallel, but workstation and benchmark dependencies must not contaminate the simulator-independent core.

## Constraints

- Do not vendor or install ROS, Gazebo, BARN, ArenaBench, Webots, MuJoCo, Stable-Baselines3, Gymnasium, NetworkX, Shapely, or similar heavyweight dependencies as part of planning.
- Do not treat PRM-RL as the full product boundary.
- Do not add broad MCP or agentic execution surfaces before stable, auditable commands exist.
- Keep external simulators, benchmarks, robotics middleware, and RL frameworks behind adapters.
