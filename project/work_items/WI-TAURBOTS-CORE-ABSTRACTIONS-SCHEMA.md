---
id: WI-TAURBOTS-CORE-ABSTRACTIONS-SCHEMA
title: Core abstractions and experiment schema
status: proposed
priority: high
owner: maintainers
workstream: core-research-harness
---

# WI-TAURBOTS-CORE-ABSTRACTIONS-SCHEMA: Core Abstractions and Experiment Schema

## Objective

Define simulator-independent core concepts and the first structured experiment/result record schema so future algorithms, simulators, and benchmarks share a stable vocabulary.

## Scope

- Specify core concepts: State/Pose/Observation/Action, World/Map/Scenario, RobotModel, Task, Policy/PolicyRunner, SimulatorBackend, RolloutEngine, Roadmap, EdgeEvaluator, Planner, Episode, EvaluationRecord, and ExperimentProfile.
- Decide the initial result format, with JSONL as the expected default unless a later design selects another simple structured format.
- Define required fields for seeds, versions, environment identity, algorithm identity, artifact paths, metrics, and run status.
- Define policy and roadmap serialization expectations at the interface level.
- Keep schemas usable by both `simple2d` and external benchmark adapters.

## Non-Goals

- Do not implement full simulator integrations or benchmark adapters.
- Do not bind schemas to a single external framework or storage engine.
- Do not claim benchmark validity before evidence-producing runs exist.

## Acceptance Criteria

- Core abstraction definitions are documented or represented in lightweight code suitable for unit tests.
- Experiment/result records can represent at least one Taurbots-native run and one future external-backend run.
- The schema preserves core/adapters separation.

## Related Workstream

- `project/workstreams/core-research-harness.md`
