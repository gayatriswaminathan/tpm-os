---
name: prioritization-engine
description: Score and rank a backlog against a chosen framework (RICE, WSJF, value vs. effort). Use when a TPM or PM needs to turn a long list of competing items into a defensible, transparent priority order.
status: planned
---

# Prioritization Engine

> **Status: planned.** The spec below is drafted; implementation is coming. Have a use case? Open an issue.

Turn a long, contested backlog into a transparent, defensible ranking — with the math shown.

## When to use this skill

- Ranking competing initiatives or features
- Defending a priority call to stakeholders with a clear rationale
- Re-scoring a backlog when new information arrives

## Inputs to ask for

1. The list of items to rank.
2. The framework to use — RICE, WSJF, or value vs. effort (default: RICE).
3. Any known values (reach, impact, effort, cost of delay).

## Output (planned)

A ranked table with each item's component scores, the computed priority, and a one-line rationale — plus a note on which inputs are estimates that should be validated.

## Operating principles (planned)

- Make the scoring transparent; show the inputs, not just the rank.
- Flag low-confidence estimates rather than hiding them in a number.
- The output is a decision aid, not a decision — surface the close calls.
