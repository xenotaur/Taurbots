# Taurbots Prompt and Execution-Record Discipline

## Purpose

Prompt IDs and execution records make prompt-driven changes traceable, searchable, reviewable, and rerunnable. Taurbots follows LRH-compatible discipline where practical, adapted to this repository's robot-navigation research-harness boundaries.

Use this guidance for meaningful prompt-driven design, planning, documentation, package, CI, algorithm, benchmark, workflow, and review-response work. Tiny obvious fixes may not need full execution-record ceremony, especially when local tooling is absent.

## Prompt ID format

Preferred prompt IDs use this form:

```text
PROMPT(<WORK_ITEM_ID_OR_AD_HOC>:<slug>)[<timestamp>]
```

Where:

- `<WORK_ITEM_ID_OR_AD_HOC>` is the applicable work item ID when one applies, otherwise `AD_HOC`;
- `<slug>` is a short descriptive slug using stable words that can be searched later; and
- `<timestamp>` is an ISO-like timestamp chosen by the prompt author, commonly UTC.

Do not rename prior prompt IDs that already follow established Taurbots or LRH-compatible practice. Preserve prompt text and IDs exactly in execution records when exact matching matters for reruns.

## Execution records

Meaningful prompt-driven PRs should create or update an execution record under `project/executions/` using:

```bash
scripts/prompts/record-execution
```

Follow `project/executions/README.md` when it exists. If the script, directory, or README is absent, document that absence in the PR summary and do not invent an incompatible replacement. A missing execution-record tool should not block a small or obvious change, but the omission must be visible to reviewers.

Execution records should normally capture:

- prompt ID;
- applicable work item or `AD_HOC`;
- date/time of execution;
- summary of changes made;
- files intentionally touched;
- validation commands run and results;
- skipped validation and why;
- rerun notes, partial-run notes, or supersession notes when applicable; and
- deviations from the prompt or repository guidance.

## Soft idempotence

Before making prompt-driven changes, search for prior execution records for the same prompt ID. Apply soft idempotence:

- do not duplicate completed work;
- preserve unrelated execution records;
- update only the record for the current prompt when appropriate;
- document reruns, partial runs, skipped work, and already-complete work clearly;
- avoid changing previous prompt records just to normalize formatting; and
- keep unrelated planning metadata out of an `AD_HOC` PR unless repository conventions require it.

Soft idempotence does not mean refusing legitimate follow-up work. It means reruns should be deliberate, reviewable, and limited to the same prompt's scope.

## Scope

Execution records are expected for meaningful prompt-driven changes to Taurbots design, planning, package structure, CI, algorithms, benchmarks, adapters, developer workflow, and other control-plane or implementation surfaces.

Execution records should not become busywork for trivial typo fixes or for repositories where execution-record tooling has not yet been added. When in doubt, create or update the record if the tooling exists and the change would matter to future agents or maintainers.

## Rerun handling checklist

For a rerun of an existing prompt ID:

1. Find the current execution record for that exact prompt ID.
2. Read the record before editing files.
3. Determine whether the requested work is already complete, partially complete, outdated, or contradicted by newer guidance.
4. Make only in-scope changes.
5. Update the current prompt's record with rerun notes, validation, and any skipped work.
