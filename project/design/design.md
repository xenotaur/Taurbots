---
id: DESIGN-CORE
title: Taurbots LRH Design
status: active
owner: maintainers
---

# Design

## Purpose
- Taurbots is being interpreted as a reproducible robot-navigation research harness with a lightweight local experiment path and a heavier Linux benchmark-preparation path.
- The LRH `project/` directory acts as the repository control plane for goals, current focus, guardrails, status, evidence, and decisions.

## Scope
- Current scope is a bootstrap control plane grounded in the README and requester-provided project context.
- The repository currently exposes minimal implementation evidence, so this design documents intended boundaries without claiming that code paths already exist.

## Core Structure
- Intent layer: principles/goal/roadmap
- Execution layer: focus/work_items/contributors
- Constraint layer: guardrails
- Truth layer: evidence/status/memory

## Repository Conceptual Layers
- Documentation and control plane: README plus LRH artifacts under `project/`.
- Lightweight experiment layer: intended Mac/Linux PRM-RL demo path that does not require ROS.
- Workstation preparation layer: intended Linux recipes/checks for ROS/Gazebo/BARN/ArenaBench readiness.
- Adapter layer: intended integration boundary for external simulators and benchmarks.

## Precedence and Interpretation Notes
- Interpret project intent in this order: principles → goal → roadmap → focus → work_items → guardrails/runtime context.
- Status claims should be constrained by evidence/status/memory and must not exceed observed repository evidence.
- Derived context files are summaries only and must not introduce commitments beyond authoritative artifacts.

## Current Implementation Boundary
- Confirmed repository evidence at bootstrap time is limited to the README, LICENSE, `.gitignore`, and this newly added LRH scaffold.
- The README identifies Taurbots as supporting clean starts for robot navigation and embodied-AI experiments.
- No source tree, recipes, tests, or simulator adapters were observed during bootstrap inspection.

## Future Extensions (Non-binding)
- Lightweight PRM-RL demo implementation and validation commands.
- Linux readiness checks for ROS/Gazebo/BARN/ArenaBench workstation setup.
- Adapter interfaces for external simulators and benchmarks.
- Evidence capture for setup checks, demo runs, and benchmark bridge validation.
