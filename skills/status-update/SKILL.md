---
name: status-update
description: Turn raw program notes into a clean, audience-ready status update. Use when a TPM needs to produce a weekly exec summary, stakeholder update, or steering-committee status from messy notes, Jira exports, or meeting takeaways. Adapts tone and depth to the audience (executive, stakeholder, or engineering).
---

# Status Update Generator

Turn raw, messy program notes into a crisp status update tailored to its audience.

## When to use this skill

Use it whenever you need to produce:

- A weekly executive summary (CIO / CTO / leadership)
- A stakeholder update (partner teams, product, business)
- A steering-committee or governance status
- A program health snapshot for a portfolio review

## Inputs to ask for

If the user hasn't provided them, ask for:

1. **Audience** — executive, stakeholder, or engineering. This sets tone and depth.
2. **Raw material** — notes, Jira/board export, last week's update, meeting takeaways, metrics.
3. **Period** — the week or reporting window this covers.
4. **Program name** and (optional) overall RAG status if already known.

If only raw notes are given, infer sensible defaults and state the assumptions made.

## Operating principles

- **Lead with the headline.** The first line is the overall status and the single most important thing leadership must know. Never bury it.
- **Audience-tune the altitude.** Executives get outcomes, risks, and decisions needed — not task-level detail. Engineering audiences get the specifics.
- **RAG with a reason.** Every Red or Amber status must name the cause and the action being taken, with an owner and date. No naked colors.
- **Surface what needs them.** Explicitly separate "FYI" from "I need a decision / unblock from you." Make asks impossible to miss.
- **Be honest, not rosy.** A status that's all green reads as low-signal. Name real risks early; that's what builds trust with leadership.
- **Quantify where possible.** "On track, 8 of 10 milestones complete" beats "going well."
- **Keep it short.** An exec update is a screenful, not a page. Cut anything that doesn't change a decision.

## Output structure

Produce the update in this shape, adjusting sections to the audience:

```
[PROGRAM NAME] — Status Update | [Period]
Overall: 🟢 / 🟡 / 🔴 — [one-line headline]

✅ Progress this period
- [Outcome-focused wins, quantified where possible]

🚧 In flight
- [What's actively moving, with target dates]

⚠️ Risks & blockers
- [Risk] → [impact] → [action / owner / date]

🙋 Decisions / help needed
- [Specific ask, who it's for, by when]

🔜 Next period
- [Top 2–3 priorities]
```

For executive audiences, keep "Progress" and "In flight" to 3–4 bullets each and make "Risks" and "Decisions needed" the focal point. For engineering audiences, expand detail and add a milestone/burn view if data allows.

## Tone

Confident, plain, and direct. Active voice. No corporate filler ("synergies," "circle back"). Write the way a trusted senior TPM briefs a busy executive: respectful of their time, clear about what matters, straight about what's at risk.

## Quality bar before returning

- Is the overall status and headline in the first two lines?
- Does every Amber/Red have a cause, an action, an owner, and a date?
- Are the asks separated from the FYIs?
- Could a reader who skims only the bold/first lines still get the picture?
- Is it the right length for the audience (exec = one screen)?

See `examples/weekly-status-example.md` for a worked example.
