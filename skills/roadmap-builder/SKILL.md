---
name: roadmap-builder
description: Build a Now / Next / Later roadmap from a list of initiatives, priorities, and constraints. Use when a TPM or PM needs to turn a messy backlog of ideas into a clear, sequenced roadmap that communicates intent and outcomes without over-promising dates.
---

# Roadmap Builder

Turn a pile of initiatives into a clear **Now / Next / Later** roadmap that sets direction and intent — without committing to false precision.

## When to use this skill

- Translating a backlog of ideas into a communicable roadmap
- Aligning stakeholders on sequence and rationale before a planning cycle
- Replacing a date-driven Gantt with an outcome-driven view leadership can read

## Inputs to ask for

If the user hasn't provided them, ask for:

1. **The initiatives** — the list of ideas, projects, or themes in play.
2. **Strategic priorities** — the goals or outcomes these should ladder up to.
3. **Constraints** — known dependencies, capacity limits, and any hard deadlines.
4. **Audience** — leadership, partner teams, or engineering (sets altitude and tone).

If inputs are thin, infer sensible placements and clearly label assumptions as `[Assumption — confirm]`.

## The horizons

- **Now** — actively in progress or starting this cycle. Highest confidence, most detail.
- **Next** — committed direction, queued behind Now. Clear intent, looser specifics.
- **Later** — real and intentional, not a graveyard. Direction without dates; revisited each cycle.

## Operating principles

- **Sequence by outcome and dependency, not by wish.** What unlocks the most value, and what must come first, decides order — not who asked loudest.
- **Every item states *why now* (or why not yet).** A roadmap without rationale invites re-litigation in every review.
- **"Later" is a respectable place.** Parking something in Later is a real decision, not a soft no. Say why it's there.
- **Avoid false precision.** Now/Next/Later communicates intent honestly. Don't bolt on dates the data can't support; if a hard date exists, call it out explicitly as a constraint.
- **Tie every item to an outcome.** Each initiative names the result it drives, not just the activity.
- **Surface the dependencies.** If an item is gated by another team or a prerequisite, show it — hidden dependencies are where roadmaps break.

## Output structure

```
# [Product / Program] Roadmap — [Date]
Theme: [the strategic thread tying this together]

## Now
- [Initiative] — outcome: [result it drives]
  Why now: [rationale] · Depends on: [dependency or "none"]

## Next
- [Initiative] — outcome: [result]
  Why next: [rationale] · Depends on: [dependency]

## Later
- [Initiative] — outcome: [result]
  Why later: [rationale / what would pull it forward]

## Notes
- Hard dates / constraints: [any genuine fixed dates]
- Key assumptions: [flagged assumptions to confirm]
```

Adjust detail to the audience: leadership gets outcomes and rationale; engineering can get dependencies and sequencing specifics.

## Tone

Clear and decisive. Each line reads like a choice was made, because one was. No hedging, no everything-is-a-priority.

## Quality bar before returning

- Is every item in a horizon for a stated reason?
- Does each initiative name an outcome, not just an activity?
- Are dependencies and any hard dates surfaced, not buried?
- Is "Later" used honestly — intentional, not a dumping ground?
- Could a leader read only the horizon headers and the "why" lines and still get the story?

See `examples/roadmap-example.md` for a worked example.
