# Example: PRD from a one-line idea

Shows the `prd-generator` skill expanding a rough idea into a structured PRD.

## Input

```
idea: let users export their dashboard data to CSV
who: analysts on the data team
why now: top request in last quarter's feedback; blocking a few renewals
constraints: web only for v1, must ship this quarter
```

## Output (generated PRD)

---

# Dashboard CSV Export — PRD

## 1. Problem
Analysts can view dashboards but can't get the underlying data out, so they re-key numbers into spreadsheets by hand. This is slow, error-prone, and was the single most-requested item in last quarter's feedback. It's now cited in two at-risk renewals.

## 2. Why now
Export is blocking renewals and is the top feedback theme. A focused v1 unblocks revenue at low build cost.

## 3. Goals
- Let an analyst export any dashboard's data to CSV in two clicks.
- Reduce manual re-keying for the data team.

## 4. Non-goals
- Scheduled/automated exports `[deferred to later]`
- Excel, PDF, or API export formats
- Mobile support (web only for v1)

## 5. Target users
Data-team analysts who consume dashboards and need the raw numbers in their own tools.

## 6. User stories
- As an analyst, I want to export a dashboard to CSV, so that I can analyze it in my own spreadsheet without re-typing.

## 7. Requirements
**Must-have (v1)**
- Export button on every dashboard
- CSV reflects current filters/date range applied to the dashboard
- Handles up to 100k rows without timing out

**Nice-to-have (later)**
- Choose columns before export
- Scheduled recurring export

## 8. Success metrics
| Metric | Baseline | Target |
|---|---|---|
| Analysts using export monthly | 0 | 40% of data team in 60 days |
| Manual re-keying tickets | ~15/mo | < 3/mo |

## 9. Acceptance criteria
- [ ] Export button appears on all dashboard types
- [ ] CSV matches the on-screen filtered data exactly
- [ ] 100k-row export completes in under 10 seconds
- [ ] Exported file opens cleanly in Excel and Google Sheets

## 10. Risks & open questions
- **Large exports may strain the query layer** → load-test at 100k rows before GA.
- **Open question:** do any dashboards contain restricted fields that shouldn't be exportable? `[Assumption — confirm with security]`

---

The skill took one line and produced a scoped, testable spec — with explicit non-goals, measurable metrics, and flagged open questions — ready for engineering review.
