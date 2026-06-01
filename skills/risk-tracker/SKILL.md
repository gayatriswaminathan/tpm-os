---
name: risk-tracker
description: Build and maintain a RAID log (Risks, Assumptions, Issues, Dependencies) for a program. Use when a TPM needs to capture, score, and track risks and issues, surface the top items for a steering review, or convert raw notes into a structured, prioritized RAID log with owners and mitigations.
---

# Risk Tracker (RAID)

Turn scattered concerns into a structured, prioritized RAID log — Risks, Assumptions, Issues, and Dependencies — that drives action.

## When to use this skill

Use it to:

- Stand up a RAID log for a new program
- Convert messy meeting notes into structured, scored entries
- Re-prioritize an existing log and surface the top items for a steering review
- Produce a "top risks" summary for an executive update

## The four categories

- **Risk** — something that *might* happen and would hurt the program. Has a probability and an impact.
- **Assumption** — something believed true that the plan depends on. If it's wrong, it becomes a risk or issue.
- **Issue** — a problem happening *now*. Certain, not probabilistic. Needs resolution, not mitigation.
- **Dependency** — something the program needs from another team/system, where a slip would block progress.

## Inputs to ask for

If not provided, ask for:

1. **Program name** and current phase.
2. **Raw material** — notes, concerns, blockers, things people are worried about.
3. Any **known owners** for items.

## Scoring

Score every Risk on **Probability** (Low/Med/High) and **Impact** (Low/Med/High), then derive severity:

| | Impact Low | Impact Med | Impact High |
|---|---|---|---|
| **Prob High** | Medium | High | Critical |
| **Prob Med** | Low | Medium | High |
| **Prob Low** | Low | Low | Medium |

Issues are scored on Impact and urgency only (they're already certain).

## Operating principles

- **Every item has a single named owner.** No owner means no action. "The team" is not an owner.
- **Every risk has a mitigation and a target date.** A risk with no mitigation is just anxiety.
- **Separate mitigation from contingency.** Mitigation reduces likelihood/impact; contingency is the plan if it happens anyway. High/Critical risks need both.
- **Promote and demote honestly.** When an assumption proves false, convert it to a risk or issue. When a risk materializes, convert it to an issue. Keep the log alive, not static.
- **Surface the vital few.** A 60-row RAID log nobody reads is useless. Always produce a "Top 5 this week" view for leadership.
- **Date everything.** Raised date, target date, last-reviewed date. Stale items are a smell.

## Output structure

Produce a table per category. Core RAID table:

```
## RAID Log — [Program] | [Date]

### 🔴 Top items this review
1. [Most important item + one-line why it matters now]
...

### Risks
| ID | Risk | Prob | Impact | Severity | Mitigation | Contingency | Owner | Target |
|----|------|------|--------|----------|------------|-------------|-------|--------|
| R1 | ... | High | High | Critical | ... | ... | ... | ... |

### Assumptions
| ID | Assumption | If false → | Owner | Validate by |
|----|------------|-----------|-------|-------------|

### Issues
| ID | Issue | Impact | Resolution | Owner | Target |
|----|-------|--------|-----------|-------|--------|

### Dependencies
| ID | We need | From | By when | Status | Owner |
|----|---------|------|---------|--------|-------|
```

## Tone

Plain and specific. Name things directly. A good RAID log is uncomfortable to read because it's honest — that's the point.

## Quality bar before returning

- Does every item have a single named owner?
- Does every Risk have a probability, impact, severity, and a mitigation?
- Do Critical/High risks also have a contingency?
- Is there a "Top items this review" summary at the top?
- Are dates present (raised / target / by-when)?

See `examples/raid-log-example.md` for a worked example.
