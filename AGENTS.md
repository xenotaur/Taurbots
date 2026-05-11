# Taurbots Agent Operating Contract

## Purpose

Taurbots is a simulator-agnostic robot-navigation research harness. It is intended to support:

- lightweight Mac/Linux algorithm development and smoke-test workflows;
- PRM-RL as the first algorithm module, not the whole product identity;
- future navigation research algorithms and baselines;
- Linux workstation preparation for heavier simulator and benchmark work; and
- adapters for external simulators and benchmarks such as Webots, MuJoCo, ROS 2/Gazebo, BARN, ArenaBench, and related systems.

This repository uses LRH-compatible project-control discipline, adapted for Taurbots. Guidance in this file is self-contained for Taurbots work; do not assume LRH implementation details are available unless the task explicitly introduces them.

## Repository boundaries

Expected repository areas may include the following, even if some do not exist yet:

```text
src/taurbots/      package code
tests/            fast tests and smoke tests
scripts/          canonical developer and validation entry points
project/          planning, design, workstreams, work items, and execution records
docs/             user/developer documentation, if present
.github/          CI workflows, if present
```

Preserve the distinction between implemented capabilities and planned capabilities. If a directory, command, adapter, or runtime feature is not present, describe it as planned or absent rather than implying it exists.

## Architectural boundary

- Core Taurbots code must remain simulator- and middleware-independent.
- ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Docker/NVIDIA, cloud, GPU, and other heavy or environment-specific assumptions belong in adapters, recipes, optional extras, documentation, smoke tests, or integration paths.
- PRM-RL is the first algorithm module. It must not become the definition of the whole Taurbots product boundary.
- External simulator, benchmark, robotics middleware, and RL-framework object models should not leak into durable core APIs unless a design explicitly accepts that coupling.

## Agent workflow

Before editing, agents should:

1. Inspect repository-local guidance, including this file, `STYLE.md`, `PROMPTS.md`, `REVIEWS.md`, affected README files, and relevant `project/` planning/design files.
2. Check for an applicable work item under `project/work_items/`. If none applies, keep the work clearly `AD_HOC`.
3. For prompt-driven work, check for prior execution records for the same prompt ID before making changes.

During implementation, agents should:

- prefer small, focused PRs;
- keep documentation and planning PRs from becoming implementation PRs;
- update affected README files when behavior, workflow, commands, or contributor expectations change;
- use canonical scripts when available, such as `scripts/develop`, `scripts/lint`, `scripts/format`, `scripts/test`, `scripts/coverage`, `scripts/smoke`, and `scripts/check-workflows`;
- keep ordinary unit tests fast, deterministic, hermetic, and Mac/Linux friendly;
- avoid installing heavy simulator, robotics, GPU, Docker/NVIDIA, benchmark, or cloud dependencies unless the task explicitly requires that layer; and
- document validation commands run, commands skipped because they are absent, and commands skipped because they require unavailable environments.

## Safety and scope

Agents should not:

- expose broad MCP, agentic, workstation-mutation, robot-control, or shell-execution surfaces without explicit design and safety boundaries;
- mutate unrelated planning files, work items, execution records, or evidence records;
- vendor external benchmark repositories casually;
- add heavyweight dependencies to the core package without explicit design justification;
- make ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Docker, NVIDIA GPUs, cloud services, or package indexes prerequisites for ordinary unit tests;
- claim benchmark validity, adapter support, simulator support, or workstation readiness without repository evidence; or
- rewrite unrelated documentation while making focused guidance or control-plane changes.

## Validation expectations

For each change, run the lightest validation that gives useful confidence. Prefer repository scripts when present. For guidance-only changes, `git status --short`, targeted file inspection, and any available lightweight lint/test scripts are usually sufficient.

If a validation command is unavailable or inappropriate for the current task, say so in the PR summary instead of inventing replacement tooling or installing heavyweight dependencies.
