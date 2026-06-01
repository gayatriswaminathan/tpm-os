---
name: prd-generator
description: Turn a feature idea or problem statement into a structured product requirements document (PRD). Use when a TPM or PM needs to scope a feature with goals, non-goals, user stories, success metrics, and acceptance criteria. Produces a clear, review-ready spec from a rough idea.
---

# PRD Generator

Turn a rough feature idea into a crisp, review-ready product requirements document.

## When to use this skill

Use it to:

- Convert a vague request ("we should let users export their data") into a scoped spec
- Pressure-test an idea before committing engineering time
- Produce a shared source of truth for product, engineering, and stakeholders
- Break a large initiative into a phased PRD

## Inputs to ask for

If not provided, ask for:

1. **The idea / problem** — what's the user pain or opportunity?
2. **Who it's for** — the target user or segment.
3. **Why now** — the business or strategic driver.
4. **Constraints** — deadlines, platforms, dependencies, or scope limits.
5. **How we'll know it worked** — any success signals the user already has in mind.

If the input is thin, draft reasonable assumptions and clearly label them as `[Assumption — confirm]`.

## Operating principles

- **Problem before solution.** Open with the user problem and evidence, not the feature. If the problem isn't clear, the PRD isn't ready.
- **Non-goals are as important as goals.** Explicitly state what's out of scope to prevent scope creep and protect the timeline.
- **Make success measurable.** Every PRD needs success metrics with a baseline and a target, not vague aspirations.
- **Acceptance criteria are testable.** Write them so QA and engineering can objectively verify "done."
- **Phase ruthlessly.** If the scope is large, propose a v1 (must-have) and defer the rest to "later" — protect the critical path.
- **Flag the unknowns.** Call out open questions and risks rather than papering over them.

## Output structure

```
# [Feature name] — PRD

## 1. Problem
[The user problem, who has it, and the evidence. 2–4 sentences.]

## 2. Why now
[Strategic / business driver. Why this is worth doing now.]

## 3. Goals
- [Outcome-focused goals — what success looks like]

## 4. Non-goals
- [Explicitly out of scope for this version]

## 5. Target users
[Primary user/segment and their key job-to-be-done]

## 6. User stories
- As a [user], I want [capability], so that [outcome].

## 7. Requirements
**Must-have (v1)**
- [Requirement]
**Nice-to-have (later)**
- [Requirement]

## 8. Success metrics
| Metric | Baseline | Target |
|---|---|---|
| [metric] | [today] | [goal] |

## 9. Acceptance criteria
- [ ] [Testable condition for "done"]

## 10. Risks & open questions
- [Risk or open question + how it will be resolved]

## 11. Rollout (optional)
[Phasing, feature-flagging, or go-to-market notes]
```

## Tone

Clear, concrete, and decisive. Short sentences. Avoid jargon and hedging. A good PRD reads like it was written by someone who has already thought hard about the edge cases.

## Quality bar before returning

- Does it open with a problem, not a solution?
- Are there explicit non-goals?
- Does every success metric have a baseline and a target?
- Are acceptance criteria objectively testable?
- Are assumptions and open questions clearly flagged?

See `examples/prd-example.md` for a worked example.
