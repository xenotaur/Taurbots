# Taurbots Style Guide

## General style

- Prefer small, focused changes with clear intent.
- Keep public APIs simple, typed, and stable enough for future adapters.
- Prefer clear dataclasses, enums, protocols, or simple typed models for core concepts once implementation begins.
- Keep documentation near the affected code, project area, command, or design record.
- Do not over-engineer plugin systems before interfaces stabilize.
- Separate planned direction from implemented behavior in docs, code comments, tests, and PR summaries.
- Favor readable names and explicit boundaries over clever abstractions.

## Architectural style

- Keep core Taurbots code simulator-independent and middleware-independent.
- Put external systems behind adapters, recipes, optional extras, or integration/smoke paths.
- Avoid leaking third-party object models into durable public APIs.
- Keep ROS messages, Gazebo entities, Webots nodes, MuJoCo models, BARN/ArenaBench conventions, Gymnasium spaces, Stable-Baselines3 policies, and NetworkX graphs out of core types unless a reviewed design explicitly justifies the coupling.
- Treat PRM-RL as the first algorithm module, not as the whole product architecture.
- Keep `simple2d`, when implemented, a lightweight smoke-test environment rather than a substitute for external benchmark validation.
- Preserve replaceable seams between core abstractions, algorithms, simulators, benchmark adapters, result records, and workstation recipes.

## Dependency style

- Keep default runtime dependencies minimal.
- Use optional extras, separated adapters, recipes, or documented environment setup for heavier dependencies.
- Avoid adding robotics, simulator, RL, GPU, Docker, cloud, or benchmark dependencies to the default install in early PRs.
- Prefer build-versus-buy decisions that preserve replaceable seams and keep the core install small.
- Do not vendor external benchmark repositories, simulator assets, or large generated artifacts casually.
- Do not make network access, package indexes, GPU drivers, Docker daemons, ROS installations, or simulator binaries prerequisites for ordinary development commands.

## Testing style

- Unit tests should be fast, deterministic, hermetic, and Mac/Linux friendly.
- Unit tests should not require ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Docker, NVIDIA GPUs, cloud access, network services, or package indexes.
- Heavy checks belong in smoke/integration scripts, optional workflows, benchmark recipes, or explicitly documented environment-specific validation.
- Local scripts and CI should run the same commands when practical.
- Prefer deterministic seeds and small fixtures for navigation, planning, and rollout tests.
- Tests should assert Taurbots-owned behavior rather than internals of external simulator or RL libraries.

## Documentation style

- Keep guidance self-contained in this repository.
- Cite repository evidence before claiming support for commands, adapters, benchmarks, workstation setup, or results.
- Update affected README files when contributor workflow, commands, dependencies, or architecture boundaries change.
- Preserve `project/` planning files as planning metadata; do not mix broad roadmap rewrites into focused implementation or guidance PRs.
- Use stable, searchable headings and filenames for prompt-driven and planning work.

## Research artifact style

Experiment and evaluation records should eventually capture:

- seeds;
- package versions;
- configuration files or hashes;
- simulator/backend identity;
- map, world, or scenario identity;
- robot model;
- algorithm and policy identity;
- metrics;
- run status;
- hardware and environment assumptions when relevant; and
- artifact paths.

Prefer stable readable formats such as JSON, JSONL, YAML, and Markdown for early artifacts. Avoid opaque binary-only artifacts as the only durable record.
