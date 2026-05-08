---
id: FOCUS-BOOTSTRAP
title: Initial LRH Bootstrap Focus
status: active
priority: high
owner: maintainers
---

# Current Focus

## Active Priority
- Establish an initial LRH control plane with grounded artifacts for Taurbots.

## Why This Appears Current
- The repository README currently gives a concise identity statement for Taurbots but does not yet expose detailed implementation files, recipes, tests, or adapter documentation.
- The requested bootstrap asks for the standard LRH `project/` scaffold and supplies the two major goals: no-ROS lightweight PRM-RL demos and Linux benchmark-preparation recipes/checks.

## Priorities
1. Keep the new LRH artifacts explicit about what is known, inferred, and unknown.
2. Preserve the two-path project direction: lightweight no-ROS experimentation and Linux benchmark readiness.
3. Define guardrails for safe, reproducible robotics setup work before adding automation that mutates systems.
4. Collect evidence as implementation files, commands, and validation workflows are added.

## Non-Goals
- Do not claim that the PRM-RL demo, readiness recipes, or adapters are implemented until repository evidence exists.
- Do not modify existing source code as part of this bootstrap.
- Do not install ROS, Gazebo, BARN, ArenaBench, or operating-system dependencies during bootstrap.
- Do not make heavyweight benchmark integrations prerequisites for the lightweight demo path.

## Exit Criteria
- The standard LRH scaffold exists under `project/`.
- Authoritative artifacts describe goal, design, guardrails, status, work item, and evidence boundaries.
- Derived human and agent contexts summarize authoritative artifacts without introducing new commitments.
- Follow-up work items are clear enough for maintainers or agents to validate and extend the harness safely.
