# Decision Log

## 2026-05-08: Bootstrap LRH project control plane

### Summary
- Created the standard LRH `project/` scaffold for Taurbots after confirming that no `project/` directory existed.

### Decisions
- Classified the repository as `new` for LRH bootstrap because `project/` was absent during inspection.
- Used the README as repository identity evidence.
- Used requester-provided context to seed the high-level project goal, including the no-ROS lightweight PRM-RL path and Linux ROS/Gazebo/BARN/ArenaBench readiness path.
- Marked implementation-specific details as TODO/unknown because source modules, recipes, tests, and adapters were not present during bootstrap inspection.
- Kept `context/humans.md` and `context/agents.md` derived and non-authoritative.

### Rationale
- The bootstrap request requires a complete standard scaffold when classification is `new`.
- Repository evidence is sufficient to verify identity, but not sufficient to claim concrete implementation capability.
- Explicit TODOs preserve project intent without inventing unsupported details.

### Uncertainty / Follow-ups
- Confirm where the lightweight PRM-RL demo will live.
- Confirm supported Mac/Linux versions and Python or robotics dependency expectations.
- Confirm supported ROS/Gazebo distributions and whether BARN/ArenaBench support will be recipes, adapters, or both.
- Confirm maintainers or code owners for each project area.

### Status
- Accepted (Bootstrap Phase)
