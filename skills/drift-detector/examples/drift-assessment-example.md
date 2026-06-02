# Example: drift assessment from program signals

Shows the `drift-detector` skill reading a busy-but-stuck program and surfacing the effort-vs-progress gap.

## Input (raw signals)

```
goal: consolidate 4 regional reporting platforms into one by year-end

last 3 status updates: all "Green"
- wk 1: kickoff complete, teams staffed, cadence established
- wk 6: 9 working groups running, architecture under review (still)
- wk 11: architecture under review (still), 2 new working groups added

activity signals:
- weekly meeting load up from 6 to 19
- 3 escalations this month, all about "alignment"
- the data-model decision has been re-opened 4 times
- steering deck grew from 8 to 31 slides

milestone progress:
- 0 of 4 platforms migrated
- architecture sign-off: still pending after 11 weeks
```

## Output (generated assessment)

---

# Drift Assessment — Reporting Platform Consolidation | Week 11
**Overall drift risk: 🔴 — busy and active, but not converting effort into progress.**
**Effort vs. progress: effort is climbing sharply (meetings 6→19, deck 8→31 slides, 3 alignment escalations) while milestone progress is flat (0 of 4 migrated, architecture unsigned for 11 weeks). This is the signal.**

## Signal scan
| Signal | Rating | Evidence |
|--------|--------|----------|
| Decision latency | 🔴 | Data-model decision re-opened 4 times; architecture sign-off pending 11 weeks. |
| Ownership diffusion | 🟡 | Escalations are about "alignment," suggesting no single owner is holding the decision. |
| Explanation overhead | 🔴 | Steering deck nearly 4x'd (8→31 slides) — more is spent explaining than deciding. |
| Recurring dependencies | 🟡 | Architecture review "still" pending across three consecutive updates. |
| Effort–progress divergence | 🔴 | Meeting load tripled; zero platforms migrated. The headline finding. |
| Outcome line-of-sight | 🔴 | Adding working groups while no platform has moved — work is expanding away from the outcome. |

## What this adds up to
This program is drifting, and it's past the early stage. Every external sign of health is present — full cadence, committed teams, "Green" status — but effort is accelerating while the outcome hasn't moved in 11 weeks. The all-Green status is masking it. The core problem is a stuck architecture decision that's spawning activity instead of progress.

## Interventions
- **Force the architecture decision to closure** — time-box it: one decider, decision by Friday, no re-opening without new information. Owner: Program lead — by: this week.
- **Freeze new working groups** until a platform migrates — stop expanding effort away from the outcome. Owner: Program lead — by: now.
- **Add an "effort vs. progress" line to the weekly status** — track migrations done against meeting/escalation load, so the divergence is visible to steering. Owner: TPM — by: next update.

---

Notice what the skill did: it ignored the reassuring "Green" status and the visible busyness, and instead surfaced the *divergence* — effort tripling while outcomes stayed at zero — then traced it to a single stuck decision and gave time-boxed, owned interventions to reconnect effort to progress.
