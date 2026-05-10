---
id: kubuntu-benchmark-workstation
title: Kubuntu Benchmark Workstation
status: active
owner: maintainers
---

# Kubuntu Benchmark Workstation

## Purpose

Prepare a Kubuntu Focus or similar Linux/NVIDIA workstation for robot-navigation research while keeping the host clean, supporting remote operation from a Mac, and enabling both modern ROS/Gazebo workflows and isolated legacy benchmark stacks.

## Scope

- SSH plus byobu/screen remote workflow assumptions.
- Tailscale-style remote access as a recommendation, not a hard product dependency.
- GPU readiness checks such as `nvidia-smi`.
- Docker and NVIDIA Container Toolkit readiness.
- Optional Apptainer/Singularity consideration for legacy benchmark stacks.
- Native modern ROS 2/Gazebo path where appropriate.
- Documentation and doctor-style diagnostics before any mutating bootstrap commands.
- Remote GUI strategy: NoMachine first, TurboVNC + VirtualGL if OpenGL visualization requires it.
- Host-versus-container boundary for legacy ROS/Gazebo stacks.

## Non-Goals

- Do not install or mutate workstation dependencies in planning PRs.
- Do not make Tailscale, NoMachine, TurboVNC, VirtualGL, Docker, Apptainer, ROS, or Gazebo hard requirements for the core local loop.
- Do not place legacy benchmark internals on the Taurbots core API path.

## First Milestones

1. Document Kubuntu Focus workstation setup strategy and operator assumptions.
2. Plan `taurbots doctor` checks for GPU, containers, ROS/Gazebo, and remote workflow readiness.
3. Define safe bootstrap and dry-run behavior before adding mutating setup commands.
4. Document remote GUI options and selection criteria.
5. Define the host/container boundary for legacy benchmark stacks.

## Initial Work Items

- `project/work_items/WI-TAURBOTS-KUBUNTU-DOCTOR-SETUP.md`

## Relationship to Adopted Design

This workstream operationalizes the adopted design's Linux workstation path while preserving Mac-friendly core development and keeping heavyweight benchmark dependencies outside the core package.
