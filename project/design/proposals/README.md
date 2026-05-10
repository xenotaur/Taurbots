# Design Proposals

Design proposals record durable architecture and scope decisions for Taurbots.

## Organization

- `adopted/` contains proposals whose frontmatter status is `adopted` and that should guide future implementation work.
- Additional buckets may be added later if the project starts tracking draft, rejected, superseded, or archived proposals.

## Metadata

A design proposal should use YAML frontmatter compatible with LRH design-proposal organization:

```yaml
---
id: stable-proposal-id
type: design_proposal
status: adopted
title: Human-Readable Proposal Title
---
```

The `id` and `status` values should be strings. Use `status: adopted` for proposals that belong in the adopted bucket.
