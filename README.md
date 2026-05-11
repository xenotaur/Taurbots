# Taurbots

Taurbots: clean starts for robot navigation and embodied-AI experiments.

The first implementation path should start with diagnostic-first Linux benchmark workstation readiness, then establish a simulator-independent core, a Mac/Linux `simple2d` PRM-RL smoke-test path, and structured results without vendoring external simulator or benchmark stacks.
Taurbots is a simulator-agnostic robot-navigation and embodied-AI research
harness. The current repository state is intentionally small: it establishes a
minimal Python package, a public CLI shape, developer scripts, and lightweight CI
so later work can add research abstractions, algorithms, simulators, benchmark
adapters, and workstation diagnostics behind clear boundaries.

## Current scope

This initial package skeleton includes:

- the `taurbots` Python package in a `src/` layout;
- a `taurbots` console script and `python -m taurbots` entry point;
- placeholder `doctor`, `prmrl`, and `benchmark` subcommands;
- lightweight developer scripts for formatting, linting, tests, coverage, smoke
  checks, and workflow validation; and
- GitHub Actions workflows for lint, tests, coverage, smoke, and workflow
  metadata checks.

The placeholder subcommands are deliberately non-functional. Robotics, PRM-RL,
simulator, benchmark, ROS/Gazebo, Webots, MuJoCo, Docker, NVIDIA, and workstation
setup functionality is deferred to later focused PRs.

## Planning

Taurbots is currently organized as a lightweight, simulator-agnostic robot-navigation research harness. The adopted architecture keeps the core research loop separate from simulator, benchmark, ROS/Gazebo, workstation, and reinforcement-learning framework details.

Start with these control-plane artifacts:

- `project/design/proposals/adopted/taurbots-research-harness-and-benchmark-workstation.md` for the adopted research-harness and benchmark-workstation design.
- `project/roadmap/roadmap.md` for staged implementation sequencing.
- `project/focus/current_focus.md` for the immediate implementation focus and explicit deferrals.
- `project/workstreams/` for the three active planning workstreams.
- `project/work_items/` for small, actionable next steps.

## Development setup

Install the package in editable mode with development dependencies:

```bash
scripts/develop
```

The developer dependency set is intentionally small and limited to local quality
checks: Ruff, Coverage.py, and PyYAML.

## CLI

After installation, the initial CLI supports:

```bash
taurbots --help
taurbots --version
python -m taurbots --help
taurbots doctor --help
taurbots prmrl --help
taurbots benchmark --help
```

Running a placeholder command without `--help` returns a non-zero status and
prints that the implementation is intentionally deferred.

## Local validation

Run the same lightweight checks used by the initial CI workflows:

```bash
scripts/format --check --diff
scripts/lint
scripts/test
scripts/coverage --html
scripts/smoke
scripts/check-workflows
```

These checks must remain independent of heavyweight robotics, simulator, GPU,
Docker, ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, and cloud tooling.

## Repository guidance

Contributors and agents should read the repository-local guidance before making changes:

- `AGENTS.md` for the agent operating contract and Taurbots boundaries;
- `PROMPTS.md` for prompt IDs and execution-record discipline;
- `REVIEWS.md` for review-response expectations; and
- `STYLE.md` for coding, testing, documentation, dependency, and research-artifact style.

