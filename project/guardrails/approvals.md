---
id: GUARDRAIL-APPROVALS
status: active
owner: maintainers
---

# Approval Guardrails

## Default Rule
- Prefer documentation, read-only checks, and dry-run validation unless a maintainer explicitly approves system-changing automation.

## Requires Maintainer Review
- Adding or changing commands that install packages, modify system services, edit shell profiles, or alter ROS/Gazebo workspaces.
- Adding benchmark adapters that depend on external repositories, large downloads, private datasets, or non-trivial licenses.
- Changing the stated project goal, scope boundaries, or guardrails.
- Marking a demo, recipe, or adapter as supported without evidence.

## Agent Approval Expectations
- Agents should keep changes narrow and cite the LRH artifact that authorizes the work.
- Agents should stop and report uncertainty rather than guessing about robotics distributions, benchmark versions, or lab-specific setup.

## TODO
- Define repository-specific reviewer names or teams once known.
