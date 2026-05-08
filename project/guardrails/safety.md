---
id: GUARDRAIL-SAFETY
status: active
owner: maintainers
---

# Safety Guardrails

## Robotics and Simulator Safety
- Treat robot-control, simulator-control, and benchmark-control commands as potentially safety-relevant.
- Do not connect to physical robots or live robot middleware without explicit documented intent and operator approval.
- Keep demo defaults local, bounded, and non-destructive.

## System Safety
- Readiness checks should report state before changing state.
- Package installation, kernel/driver changes, GPU/CUDA changes, and service changes require explicit documentation and review.
- Scripts should avoid destructive filesystem operations and should clearly identify paths they read or write.

## Research Safety
- Do not present unvalidated experiment results as benchmark conclusions.
- Record assumptions about maps, seeds, simulators, and dependency versions when evidence is added.

## Initial Bootstrap Boundary
- This bootstrap adds documentation/control-plane artifacts only; it does not run robotics workloads or install dependencies.
