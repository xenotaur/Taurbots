---
id: WI-BOOTSTRAP-0001
title: Bootstrap LRH project control plane
status: complete
priority: high
owner: automation
created: 2026-05-08
---

# WI-BOOTSTRAP-0001: Bootstrap LRH Project Control Plane

## Objective
- Create the standard LRH `project/` scaffold for Taurbots without modifying existing source files.

## Scope
- Add authoritative LRH artifacts for principles, goal, roadmap, design, focus, contributors, guardrails, evidence, status, and memory.
- Add derived context summaries for humans and agents.
- Ground claims in the README and requester-provided context.

## Acceptance Criteria
- `project/` contains the standard LRH bootstrap artifacts.
- Uncertain implementation details are marked as TODOs or unknowns.
- Derived context files remain non-authoritative.
- No files outside `project/` are modified.

## Evidence
- See `project/evidence/EV-0001.md` for bootstrap inspection evidence.

## Status
- Complete for initial bootstrap.
- Follow-up work should replace TODOs with evidence-backed implementation details as the repository grows.
