# Taurbots Review-Response Guidance

## Purpose

Review-response work should improve the current PR without changing its identity. Taurbots review handling preserves the adopted core/adapters architecture, keeps validation lightweight when possible, and distinguishes implemented capabilities from planned research-harness direction.

## Review-response principles

Agents responding to review feedback should:

- inspect each review comment carefully before editing;
- decide whether each requested change is already present, valid, feasible, and in scope;
- implement only changes that belong in the current PR;
- ask maintainers or document uncertainty when feedback conflicts with adopted design or current repository evidence;
- avoid broad unrelated refactors;
- preserve Taurbots' simulator-independent core and adapter boundaries;
- update affected README or project documentation when review changes affect workflow, design, validation, or contributor expectations; and
- run relevant validation after changes.

If a review asks for work outside the PR scope, note the boundary and suggest a follow-up work item or PR rather than silently expanding the change.

## Taurbots-specific guidance

When addressing review comments:

- Do not satisfy feedback by adding heavy simulator, robotics, RL, Docker/NVIDIA, GPU, benchmark, or cloud dependencies unless the PR explicitly concerns that layer.
- Distinguish documentation issues, recipe issues, optional-dependency issues, adapter issues, and unavailable-environment issues.
- Avoid moving ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Gymnasium, Stable-Baselines3, NetworkX, or benchmark-specific assumptions into core code.
- Keep Mac/Linux-friendly unit tests separate from heavy simulator, GPU, Docker, ROS, or benchmark smoke/integration checks.
- Preserve PRM-RL as the first algorithm module, not as the whole Taurbots identity.
- Do not claim benchmark parity, simulator support, workstation readiness, or scientific validity without repository evidence.
- Prefer documenting a limitation or future adapter boundary over introducing a premature abstraction that locks Taurbots to one backend.

## Validation

Use canonical scripts when available and appropriate, such as:

```bash
scripts/lint
scripts/test
scripts/smoke
scripts/check-workflows
```

For documentation-only changes, targeted file inspection plus lightweight available scripts may be enough. Do not install ROS, Gazebo, Webots, MuJoCo, BARN, ArenaBench, Docker/NVIDIA tooling, cloud tools, or package indexes solely to answer a review unless the PR is explicitly about that environment.

In the PR response or summary, document:

- validation commands that passed;
- commands that failed, with the failure reason;
- commands that were skipped because they were absent;
- commands that were skipped because they require unavailable heavyweight environments; and
- any review requests intentionally deferred as out of scope.
