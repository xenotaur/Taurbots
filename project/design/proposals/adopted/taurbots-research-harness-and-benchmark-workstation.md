---
id: taurbots-research-harness-and-benchmark-workstation
type: design_proposal
status: adopted
title: Taurbots Research Harness and Benchmark Workstation Architecture
---

# Taurbots Research Harness and Benchmark Workstation Architecture

## Summary

Taurbots is a simulator-agnostic robot-navigation research harness. Its first implementation direction is intentionally narrow: provide a lightweight PRM-RL reproduction path, a Mac/Linux smoke-test simulator for fast algorithm iteration, and reproducible setup recipes for Linux benchmark stacks.

The adopted architecture keeps the research core separate from simulator, benchmark, robotics middleware, and reinforcement-learning framework details. Taurbots should support:

- a lightweight Mac/Linux research loop for algorithm development and smoke tests;
- Linux workstation preparation for heavier simulators, GPU workloads, ROS/Gazebo stacks, and benchmark runs;
- containerized recipes for version-sensitive benchmark stacks, including legacy Ubuntu, ROS, and Gazebo combinations when necessary;
- adapter-oriented growth toward Webots, MuJoCo, ROS 2/Gazebo, BARN, ArenaBench, and related environments; and
- PRM-RL as the first algorithm module, not the entire product identity.

Adopting this proposal does not mean all runtime packages, commands, adapters, or algorithms already exist. It records the intended boundaries so future implementation PRs can add capabilities without turning Taurbots into a simulator-specific or benchmark-specific monolith.

## Motivation

Robot-navigation research stacks are often difficult to reproduce. Papers, benchmark repositories, simulator plugins, ROS packages, and reinforcement-learning dependencies may require exact versions of Ubuntu, ROS, Gazebo, CUDA, Python, PyTorch, or simulator binaries. Even when code is available, reproducing results can depend on undocumented shell history, workstation-specific GPU setup, or fragile combinations of archived packages.

Taurbots addresses the gap between local research iteration and serious benchmark validation:

- Mac users need lightweight local smoke tests and algorithm development workflows that do not require ROS, Gazebo, NVIDIA drivers, or a dedicated robotics workstation.
- Full training, simulation, and benchmarking often require Linux, NVIDIA GPUs, containers, ROS/Gazebo, or cloud instances.
- Older benchmark stacks often pin to legacy ROS, Gazebo, or Ubuntu versions and are hard to run safely on a modern host without containers or isolated environments.
- Researchers need a clean bridge from toy/local experiments to serious benchmark environments, with evidence that results, seeds, versions, artifacts, and hardware assumptions were captured.

The core problem is not merely running one simulator. The problem is preserving a clean research harness that can start small, remain reproducible, and later validate experiments against community benchmarks.

## Scope

The initial Taurbots scope includes documentation, interfaces, and implementation paths for:

- diagnostic and setup guidance for a Linux robotics workstation such as a Kubuntu Focus;
- SSH, byobu, screen, and Tailscale-style remote operation as infrastructure assumptions and operator practices, not hard product dependencies;
- Docker, NVIDIA Container Toolkit, and optional Apptainer/Singularity-style containers for benchmark stacks that need version isolation;
- a native modern ROS 2/Gazebo path where appropriate, especially when benchmark or adapter work benefits from current tooling;
- a lightweight, Mac-friendly PRM-RL research path that can run without ROS or heavyweight simulators; and
- adapter contracts and result schemas that preserve portability between simple local experiments and external benchmark validation.

This proposal also scopes the design conversation around a future-friendly architecture. It does not require the first implementation PR to create every package, directory, or class named below.

## Non-goals for v0

Taurbots v0 should explicitly avoid:

- replacing ROS, Gazebo, Webots, MuJoCo, BARN, or ArenaBench;
- becoming a general-purpose simulator;
- implementing a full Nav2 replacement;
- automatically provisioning arbitrary cloud infrastructure;
- exposing broad MCP or agentic control surfaces before stable scripts, operator confirmations, and safety boundaries exist; and
- maintaining legacy benchmark internals as Taurbots-owned APIs.

Legacy benchmark repositories and simulator integrations may be wrapped, invoked, configured, or validated by Taurbots, but their internal APIs should remain external unless Taurbots deliberately adopts a stable adapter boundary.

## Architectural principles

1. **Core before adapters**: core research types and algorithms should not depend on ROS, Gazebo, BARN, ArenaBench, Webots, MuJoCo, Gymnasium, Stable-Baselines3, or NetworkX object models.
2. **Adapters are replaceable**: simulators, benchmark stacks, RL frameworks, graph libraries, and robotics middleware should be adapter-backed.
3. **PRM-RL is the first algorithm, not the product boundary**: Taurbots should later support additional navigation algorithms, baselines, human-aware navigation, learned local planners, and multi-agent/social navigation.
4. **Mac-friendly does not mean Mac-limited**: local development should run on Mac, but training and benchmark sweeps should scale to Kubuntu, Linux workstation, or AWS-like hosts.
5. **ROS is optional at the core**: ROS messages and launch assumptions belong in optional adapters.
6. **Benchmarks are validation backends**: BARN and ArenaBench should validate Taurbots experiments, not define Taurbots internals.
7. **Reproducibility is a first-class feature**: experiment records, result schemas, artifact paths, seeds, package versions, and hardware profiles should be tracked early.
8. **Safe defaults**: initial automation should be diagnostic and recipe-oriented; broad agentic or MCP execution should wait for stable commands and safety boundaries.

## Proposed package shape

A future-friendly Taurbots package could evolve toward the following shape:

```text
taurbots/
  core/
    types.py
    simulation.py
    tasks.py
    policies.py
    rollout.py
    experiments.py
    metrics.py

  algorithms/
    prm_rl/
      roadmap.py
      edge_eval.py
      planner.py

  envs/
    simple2d/
      backend.py
      gym_adapter.py

  adapters/
    ros2/
    webots/
    mujoco/
    barn/
    arena/

  benchmarks/
    registry.py
    recipes/

  cli/
    doctor.py
    bootstrap.py
    benchmark.py
    prmrl.py
```

This structure is a design direction, not a requirement that the first implementation PR create all directories. Early PRs may start with a smaller subset as long as they preserve the core/adapters boundary and avoid placing simulator-specific assumptions into the deepest research abstractions.

## Core abstractions

The Taurbots core should eventually represent the following concepts independently of any one simulator:

- **State / Pose / Observation / Action**: portable data shapes for robot state, robot pose, observations, and commands.
- **World / Map / Scenario**: descriptions of navigable spaces, obstacles, semantic context, starts, goals, and dynamic actors.
- **RobotModel**: physical and kinematic assumptions needed by planning, rollout, collision checking, and policy execution.
- **Task**: a navigation objective, success condition, timeout, reset behavior, and metric set.
- **Policy / PolicyRunner**: policy definitions and execution wrappers that can run learned, scripted, or hybrid behaviors.
- **SimulatorBackend**: a minimal interface for reset, step, render, state extraction, and environment metadata.
- **RolloutEngine**: the orchestration layer that runs policies against tasks in a simulator backend and records outcomes.
- **Roadmap**: a Taurbots-owned representation of sampled configurations, graph connectivity, and planning metadata.
- **EdgeEvaluator**: the component that estimates traversability, cost, success likelihood, or learned value for roadmap edges.
- **Planner**: an algorithm that chooses routes or actions from a task, roadmap, robot model, and evaluator.
- **Episode**: one attempted task execution, including initial conditions, trajectory, events, termination reason, and metrics.
- **EvaluationRecord**: a structured record of benchmark, task, policy, result, artifact, and environment details.
- **ExperimentProfile**: a reproducible bundle of seeds, configuration, dependency versions, hardware profile, and artifact layout.

Gymnasium is useful as an RL-facing compatibility layer, especially for reusing RL tooling and baselines. It should be treated as an adapter around Taurbots concepts rather than the deepest internal abstraction.

## Initial implementation path

Implementation should proceed incrementally:

1. Add `taurbots doctor`-style diagnostics and setup documentation for host readiness.
2. Add a `simple2d` Mac/Linux smoke-test simulator for local algorithm iteration without ROS.
3. Add the PRM-RL algorithm module using the simple simulator.
4. Add a structured experiment and result schema for episodes, metrics, seeds, versions, and artifacts.
5. Add benchmark recipes for BARN ROS 2 and ArenaBench containers.
6. Add an optional Webots or MuJoCo adapter after the core smoke-test path is stable.
7. Add ROS 2/Gazebo adapter support and benchmark validation flows.
8. Add later MCP or agentic wrappers only around stable, auditable commands with clear safety boundaries.

Each step should produce evidence through lightweight checks, recorded commands, result files, or documentation that future agents and maintainers can inspect.

## Workstreams

Initial workstreams are:

- **Core research harness**: simulator-independent abstractions, experiment schemas, and the PRM-RL implementation.
- **Kubuntu benchmark workstation**: Linux host setup, GPU/container checks, ROS/Gazebo readiness, and remote workflow documentation.
- **External simulator and benchmark adapters**: BARN, ArenaBench, ROS 2/Gazebo, Webots, and MuJoCo integration points.
- **Reproducibility and evidence**: result records, artifact layout, seeds, dependency versions, and hardware profile capture.
- **Future agentic/MCP tooling**: deferred until stable command boundaries exist and safety assumptions are documented.

These workstreams may proceed in parallel as long as they do not collapse into a single dependency-heavy runtime path.

## Build-versus-buy choices

The likely early build-versus-buy choices are:

- Build Taurbots core abstractions and PRM-RL-specific logic.
- Buy or use Gymnasium as an RL-facing environment API where useful.
- Buy or use Stable-Baselines3 or similar libraries initially for RL algorithms when they accelerate reproducible baselines.
- Buy or use NetworkX initially for graph operations behind Taurbots-owned roadmap interfaces.
- Buy or use Shapely or simple NumPy/grid collision logic for early geometry, depending on the smoke-test simulator needs.
- Use Webots and MuJoCo as optional simulator backends when useful for development, visualization, or physics coverage.
- Use ROS 2/Gazebo for Linux validation and community benchmark compatibility.
- Use Docker, NVIDIA Container Toolkit, and optional Apptainer/Singularity-style containers for legacy benchmark stacks.

The important boundary is that purchased or external libraries should sit behind Taurbots-owned interfaces where they are likely to change or impose heavyweight dependencies.

## Compatibility with other Logical Robotics packages

Taurbots should fit into the Logical Robotics / Anthony Francis package constellation without forcing every package to be a runtime dependency:

- **LRH** can manage workstreams, work items, design proposals, and prompt/execution discipline.
- **Taurworks** can manage project and workspace setup at a general level.
- **Taurcode** can carry reusable robotics and benchmark prompt packs.
- **Prosoc** may become relevant for social or human-aware navigation and agent behavior constraints.
- **LCATS** is not a core dependency, but may later relate to scenario or narrative structure if Taurbots grows toward embodied task stories.

Integration should be opportunistic and explicit. Taurbots should support LRH-style project discipline without making LRH internals necessary for running core experiments.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Scope creep into a universal robotics platform. | Keep v0 anchored to a lightweight research harness, PRM-RL, host diagnostics, and benchmark recipes; require new simulator or benchmark work to pass through adapter boundaries. |
| Dependency sprawl from mixing ROS 1, ROS 2, Gazebo Classic, Gazebo Harmonic, benchmark forks, and Python RL stacks. | Prefer optional extras, containers, and recipe-specific environments; keep the core install small and simulator-independent. |
| Over-coupling to PRM-RL, Gymnasium, ROS, NetworkX, Stable-Baselines3, or a single simulator. | Define Taurbots-owned core abstractions and treat those technologies as algorithms, adapters, or implementation details. |
| Fragile legacy benchmark environments. | Capture exact versions, container images, patches, setup commands, and validation evidence; avoid rewriting benchmark internals as Taurbots APIs. |
| Remote-desktop and GPU visualization complexity. | Treat SSH/byobu/screen/Tailscale-style workflows as documented operating practices; keep visualization optional for diagnostics and benchmark runs. |
| Unsafe premature MCP or agentic controls. | Start with read-only diagnostics and documented recipes; expose agentic wrappers only around stable commands with explicit safety boundaries. |

## Open questions

These questions do not block adoption, but should guide follow-up work:

- Should the first non-`simple2d` simulator adapter be Webots or MuJoCo?
- Should benchmark recipes live in the core package, optional extras, or a separate recipes area?
- Should Taurbots begin as one package with extras or split packages later?
- Should JSONL be the initial canonical result format, with Parquet considered later for larger benchmark sweeps?
- How much LRH integration should Taurbots require versus support opportunistically?
- Which benchmark stack should be the first fully reproducible external validation target?

## Consequences

Adopting this proposal means:

- Taurbots has a durable core/adapters architecture to guide future implementation PRs.
- PRM-RL can proceed as the first algorithm without constraining the long-term research platform.
- Kubuntu, ArenaBench, and BARN setup can proceed as a parallel workstream without contaminating the Mac-friendly research core.
- Future work can be planned as workstreams and implementation PRs, with reproducibility and evidence capture treated as first-class project requirements.
