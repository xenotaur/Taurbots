# Work Items

Work items are small, actionable planning or implementation units. They should be narrow enough for a future PR to complete or make measurable progress without creating a giant backlog.

Use existing LRH-style frontmatter when adding items:

```yaml
---
id: WI-TAURBOTS-EXAMPLE
status: proposed
title: Example work item
workstream: core-research-harness
---
```

Current proposed items are intentionally planning-sized and should guide the next implementation prompts. Keep completed or superseded status updates in the individual item files rather than editing unrelated historical records.

## Organization

The repository currently keeps work items in this directory as a flat list. Add `proposed/`, `active/`, `resolved/`, or `abandoned/` buckets only when the backlog grows enough to justify them; until then, use the `status` frontmatter field as the source of truth.

For current sequencing, read:

- `project/roadmap/roadmap.md`
- `project/focus/current_focus.md`
- `project/workstreams/README.md`

The initial Taurbots planning set is intentionally small:

- `WI-TAURBOTS-CORE-SKELETON.md`
- `WI-TAURBOTS-CORE-ABSTRACTIONS-SCHEMA.md`
- `WI-TAURBOTS-SIMPLE2D-PRMRL-SMOKE.md`
- `WI-TAURBOTS-KUBUNTU-DOCTOR-SETUP.md`
- `WI-TAURBOTS-BENCHMARK-ADAPTERS-RECIPES.md`
