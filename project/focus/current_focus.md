---
id: FOCUS-PLANNING-WORKSTREAMS
title: Planning Workstreams and First Implementation Focus
status: active
priority: high
owner: maintainers
---

# Current Focus

## Active Priority

Establish Taurbots planning and scaffold the first implementation around a simulator-independent core, a Mac/Linux `simple2d` PRM-RL path, and Linux benchmark workstation readiness.

## Why This Is Current

- The adopted research-harness design defines Taurbots as simulator-agnostic and explicitly separates core concepts from external simulator, benchmark, ROS/Gazebo, and RL-framework details.
- The repository now needs actionable control-plane artifacts so future implementation PRs can add code without re-litigating architecture boundaries.
- The highest-value near-term path is a small, testable core and a lightweight local loop, with workstation and benchmark work proceeding through diagnostics and recipes.

## Immediate Priorities

1. Plan Kubuntu workstation readiness checks before any mutating bootstrap commands.
2. Define the core package skeleton, CLI direction, tests/docs conventions, and dependency guardrails.
3. Plan the `simple2d` smoke-test environment and PRM-RL baseline workflow for later implementation.
4. Define simulator-independent core abstractions and the initial experiment/result schema.
5. Define the external benchmark adapter contract and first BARN ROS 2 / ArenaBench recipe plans.

## Explicit Deferrals

- Full benchmark automation is deferred until adapter contracts, recipes, and normalized result records are stable.
- Cloud orchestration is deferred.
- Broad MCP or agentic execution is deferred until commands are stable, auditable, and safety-bounded.
- Full ROS/Gazebo integration is deferred until the core schema and adapter boundary are in place.
- Webots or MuJoCo implementation is deferred unless a focused design spike selects one as the first non-`simple2d` adapter.

## Exit Criteria

- Roadmap, workstreams, and initial work items identify the next implementation PRs.
- Future implementation prompts can choose a small work item without creating duplicate planning systems.
- Planning remains aligned with `project/design/proposals/adopted/taurbots-research-harness-and-benchmark-workstation.md`.
