---
id: GOAL-CORE
title: Reproducible Robot-Navigation Research Harness
status: active
owner: maintainers
time_horizon: long
---

# Project Goal

## Objective

Taurbots is intended to be a reproducible robot-navigation research harness for cleanly setting up benchmark environments, running lightweight PRM-RL experiments, and connecting those experiments to external simulators and benchmarks through adapters.

## Intended Outcome
- Researchers can run a lightweight PRM-RL demo on Mac or Linux without requiring ROS.
- Researchers can use Taurbots recipes and checks to prepare Linux workstations for ROS, Gazebo, BARN, and ArenaBench work.
- The repository provides clear boundaries between portable local experiments, Linux benchmark preparation, and external simulator/benchmark integrations.
- Setup and validation steps are explicit enough to support repeatable research workflows.

## Intended Users / Stakeholders
- Robotics and embodied-AI researchers evaluating navigation experiments.
- Developers maintaining lightweight PRM-RL demos and benchmark adapters.
- Lab operators preparing Linux workstations for ROS/Gazebo/BARN/ArenaBench workflows.
- AI agents and automation tools that need a grounded project control plane before making changes.

## In Scope
- Lightweight Mac/Linux PRM-RL experiment workflows that do not require ROS.
- Linux workstation readiness recipes and checks for serious ROS/Gazebo/BARN/ArenaBench use.
- Adapter boundaries for bridging local experiments to external simulators and benchmarks.
- Documentation and evidence artifacts that make setup, validation, and project state auditable.

## Out of Scope (Initial)
- Replacing ROS, Gazebo, BARN, ArenaBench, or other external benchmark projects.
- Requiring ROS for the lightweight local PRM-RL demo path.
- Undocumented system mutation as part of setup or validation.
- Claiming benchmark parity, performance, or scientific validity without evidence in the repository.

## Success Direction
- A new contributor can identify the lightweight no-ROS path, the Linux benchmark-preparation path, and the adapter boundary from repository documentation.
- Environment checks and recipes can be run reproducibly and report actionable readiness results.
- Project status remains evidence-backed and distinguishes implemented behavior from planned or inferred behavior.
