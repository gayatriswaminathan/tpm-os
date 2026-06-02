---
name: drift-detector
description: Detect program drift — the gradual separation between effort and progress — before a program is formally at risk. Use when a TPM or leader wants an early read on whether a busy, active-looking program has quietly stopped converting effort into outcomes.
---

# Drift Detector

Catch **program drift** early — the gap between *activity* and *progress* — before it becomes a formal at-risk status.

## The core idea

A program rarely fails in a single moment. It drifts. From the outside it still looks healthy: executive attention, active workstreams, committed teams, a full operating cadence. The trouble is that the activity has quietly stopped converting into progress.

The clearest signal is counterintuitive: **effort goes up while progress flattens.** As a program drifts, people often work *harder* — more aligning, explaining, escalating, documenting, and defending the work. The calendar fills; the outcome doesn't get closer. This skill looks for that divergence and the tells that precede it.

## When to use this skill

- A monthly or quarterly health check on an important program
- A gut-check when a program "feels" busy but stuck
- Preparing a candid read for a steering committee before status formally turns Amber/Red
- Onboarding to a program and wanting to assess its real trajectory

## Inputs to ask for

If not provided, ask for:

1. **The original goal / outcome** the program was chartered to deliver.
2. **Recent status updates** (last 3–6), to see the trend, not a snapshot.
3. **The RAID log** (or list of risks, issues, dependencies).
4. **Activity signals** if available — meeting load, escalations, decision turnaround, churn on decisions, action-item age.
5. **Milestone/outcome progress** — what has actually moved toward the goal.

If data is thin, assess what you can and clearly state what's missing.

## The six drift signals

Assess each, with specific evidence, and rate it Green / Amber / Red:

1. **Decision latency** — are decisions taking longer than they should, or getting re-opened after they're made?
2. **Ownership diffusion** — is it getting harder to name a single owner for decisions and outcomes?
3. **Explanation overhead** — do updates need more justifying and defending than they used to? Rising narrative effort is a tell.
4. **Recurring dependencies** — do the same dependencies keep resurfacing without resolving?
5. **Effort–progress divergence (the core signal)** — is activity rising (meetings, escalations, documents, re-litigated decisions) while milestone progress flattens?
6. **Outcome line-of-sight** — can the team still draw a straight line from this week's work to the chartered outcome? When that line gets fuzzy, drift is underway.

## Operating principles

- **Trend over snapshot.** Drift only shows up across time. Always compare the last several updates, not the latest one.
- **Busyness is a symptom, not health.** Treat rising effort with flat progress as a red flag, not reassurance.
- **Name it before it's "at risk."** The value is calling it early, while it's still uncomfortable rather than obvious.
- **Separate caring from converting.** Teams that are drifting often care intensely and work hard. This is not a people problem; it's a conversion problem. Frame it that way.
- **Every finding points to an intervention.** Diagnosis without a next move is just anxiety. Each flagged signal gets a specific, owner-assigned corrective action.

## Output structure

```
# Drift Assessment — [Program] | [Date]
Overall drift risk: 🟢 / 🟡 / 🔴 — [one-line read]
Effort vs. progress: [is effort rising while progress flattens? the headline finding]

## Signal scan
| Signal | Rating | Evidence |
|--------|--------|----------|
| Decision latency | 🟡 | ... |
| Ownership diffusion | ... | ... |
| Explanation overhead | ... | ... |
| Recurring dependencies | ... | ... |
| Effort–progress divergence | ... | ... |
| Outcome line-of-sight | ... | ... |

## What this adds up to
[2–3 sentences: is this program drifting, and how far along?]

## Interventions
- [Specific corrective action] — owner: [name] — by: [date]
```

## Tone

Direct and non-alarmist. Drift is normal and recoverable when caught early. The job is to make the invisible visible, not to assign blame.

## Quality bar before returning

- Did you assess the *trend* across multiple updates, not a single snapshot?
- Is the effort-vs-progress divergence called out explicitly as the headline?
- Does every Amber/Red signal have concrete evidence?
- Does every finding map to a specific, owned intervention?
- Is the framing "conversion problem," not "blame the team"?

See `examples/drift-assessment-example.md` for a worked example.

---

*Concept credit: this skill operationalizes the idea of "program drift — the gradual separation between effort and progress" as articulated by Michael Bigenwald (2026). It turns that diagnosis into a repeatable early-detection check.*
