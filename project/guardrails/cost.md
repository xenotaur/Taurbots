---
id: GUARDRAIL-COST
status: active
owner: maintainers
---

# Cost Guardrails

## Compute and Storage
- Keep lightweight PRM-RL demos runnable on ordinary Mac/Linux development machines when possible.
- Heavyweight benchmark workflows should state expected CPU, GPU, disk, memory, and runtime requirements before users run them.
- Avoid surprise downloads of large datasets, simulator assets, containers, or model artifacts.

## External Services
- Do not require paid services for the lightweight demo path unless explicitly approved and documented.
- If optional cloud or hosted resources are introduced later, document cost risk and local alternatives.

## Dependency Cost
- Prefer checks that explain missing dependencies before installing them.
- Keep ROS/Gazebo/BARN/ArenaBench setup recipes explicit about version and disk/network impact.

## TODO
- Add measured resource expectations once demos and readiness checks exist.
