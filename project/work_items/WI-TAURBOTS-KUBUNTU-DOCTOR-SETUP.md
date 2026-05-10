---
id: WI-TAURBOTS-KUBUNTU-DOCTOR-SETUP
title: Kubuntu workstation doctor and setup documentation
status: proposed
priority: medium
owner: maintainers
workstream: kubuntu-benchmark-workstation
---

# WI-TAURBOTS-KUBUNTU-DOCTOR-SETUP: Kubuntu Workstation Doctor and Setup Documentation

## Objective

Document and later implement diagnostic-first workstation readiness checks for a Kubuntu Focus or similar Linux/NVIDIA robot-navigation benchmark machine.

## Scope

- Document SSH plus byobu/screen remote operation assumptions.
- Recommend Tailscale-style access as an option, not a hard dependency.
- Plan checks for `nvidia-smi`, Docker, NVIDIA Container Toolkit, optional Apptainer/Singularity, ROS 2/Gazebo readiness, and remote GUI options.
- Define safe bootstrap behavior with dry-run defaults and clear operator confirmation before mutating commands.
- Document NoMachine as the first remote GUI strategy, with TurboVNC + VirtualGL as a fallback when OpenGL visualization requires it.
- Define host-versus-container boundaries for modern native ROS 2/Gazebo and legacy benchmark stacks.

## Non-Goals

- Do not install drivers, containers, ROS, Gazebo, or remote GUI tools in this planning item.
- Do not require workstation tooling for the core `simple2d` path.
- Do not expose broad agentic workstation mutation surfaces.

## Acceptance Criteria

- Workstation setup strategy is documented before mutation scripts are added.
- Diagnostic checks distinguish installed, missing, misconfigured, and skipped states.
- Bootstrap plans include dry-run and safety-boundary expectations.

## Related Workstream

- `project/workstreams/kubuntu-benchmark-workstation.md`
