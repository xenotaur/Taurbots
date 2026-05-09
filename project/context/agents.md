# Project Context (Agent-Oriented)

## Mission Summary
- Taurbots is intended as a reproducible robot-navigation research harness.
- Preserve two project paths:
  1. lightweight Mac/Linux PRM-RL demos without ROS;
  2. Linux workstation recipes/checks for ROS/Gazebo/BARN/ArenaBench readiness.
- Keep external simulator and benchmark bridges behind clean adapters.

## Authoritative Artifact Map
- Read first for project direction: `project/principles/principles.md`, then `project/goal/project_goal.md`.
- Read for current planning: `project/roadmap/roadmap.md`, `project/focus/current_focus.md`, and `project/work_items/WI-BOOTSTRAP-0001.md`.
- Read before making risky changes: `project/guardrails/approvals.md`, `project/guardrails/safety.md`, `project/guardrails/cost.md`, and `project/guardrails/optics.md`.
- Read for truth state: `project/evidence/EV-0001.md`, `project/status/current_status.md`, and `project/memory/decision_log.md`.
- Treat this file and `project/context/humans.md` as derived, non-authoritative summaries.

## Execution Constraints
- Do not invent implemented capabilities; cite evidence before claiming demos, checks, adapters, or benchmark support work.
- Do not make ROS/Gazebo/BARN/ArenaBench prerequisites for the lightweight no-ROS demo path.
- Prefer read-only checks and dry-run documentation before system-changing setup automation.
- Avoid installing packages, mutating OS state, connecting to robots, or running heavyweight simulators without explicit scoped authorization and documentation.

## Confidence / Uncertainty Notes
- High confidence: repository identity is Taurbots; LRH bootstrap was appropriate because `project/` was absent.
- Medium confidence: the two-path project direction is authoritative for this bootstrap because it was provided in the request.
- Low confidence: concrete implementation layout, runnable commands, dependency versions, and adapter status, because these were not present in repository evidence during bootstrap.

## Derived Summary Boundary
- This file is derived from `project/context/humans.md` and the authoritative artifacts it summarizes.
- If uncertain, stop, report the uncertainty, and update evidence/status only after validation.
