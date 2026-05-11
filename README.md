# Taurbots

Taurbots: clean starts for robot navigation and embodied-AI experiments.

## Planning

Taurbots is currently organized as a lightweight, simulator-agnostic robot-navigation research harness. The adopted architecture keeps the core research loop separate from simulator, benchmark, ROS/Gazebo, workstation, and reinforcement-learning framework details.

Start with these control-plane artifacts:

- `project/design/proposals/adopted/taurbots-research-harness-and-benchmark-workstation.md` for the adopted research-harness and benchmark-workstation design.
- `project/roadmap/roadmap.md` for staged implementation sequencing.
- `project/focus/current_focus.md` for the immediate implementation focus and explicit deferrals.
- `project/workstreams/` for the three active planning workstreams.
- `project/work_items/` for small, actionable next steps.

The first implementation path should start with diagnostic-first Linux benchmark workstation readiness, then establish a simulator-independent core, a Mac/Linux `simple2d` PRM-RL smoke-test path, and structured results without vendoring external simulator or benchmark stacks.
