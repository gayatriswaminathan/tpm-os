# Example: RAID log from raw notes

Shows the `risk-tracker` skill turning concerns into a structured, scored RAID log.

## Input (raw notes)

```
program: Payments Migration, phase: build

notes:
- worried the vendor API won't be ready in time, they've slipped before
- we're assuming the old system stays up until cutover — nobody confirmed
- the staging environment has been down for 3 days, blocking testing
- need the security team to finish the pen test before go-live
- if peak traffic hits during migration we could overload the queue
```

## Output (generated RAID log)

---

## RAID Log — Payments Migration | Build phase

### 🔴 Top items this review
1. **Staging down 3 days (I1)** — actively blocking all test progress; needs resolution today.
2. **Vendor API readiness (R1)** — Critical; prior slips make this the biggest schedule threat.
3. **Pen test dependency (D1)** — hard gate on go-live; confirm the date now, not later.

### Risks
| ID | Risk | Prob | Impact | Severity | Mitigation | Contingency | Owner | Target |
|----|------|------|--------|----------|------------|-------------|-------|--------|
| R1 | Vendor API not ready by integration window | High | High | Critical | Weekly checkpoint with vendor; request firm date in writing | Build a stub to test against; hold a 1-week schedule buffer | G. Swaminathan | Jun 15 |
| R2 | Peak traffic during migration overloads the queue | Med | High | High | Schedule cutover in low-traffic window; load-test the queue | Throttle + auto-scale plan ready to trigger | Eng lead | Jun 20 |

### Assumptions
| ID | Assumption | If false → | Owner | Validate by |
|----|------------|-----------|-------|-------------|
| A1 | Legacy system stays live until cutover | Becomes a Critical issue — no fallback during migration | G. Swaminathan | Jun 5 |

### Issues
| ID | Issue | Impact | Resolution | Owner | Target |
|----|-------|--------|-----------|-------|--------|
| I1 | Staging environment down 3 days | Blocks all integration testing | Escalate to infra; restore or provision alternate env | Infra on-call | Jun 2 |

### Dependencies
| ID | We need | From | By when | Status | Owner |
|----|---------|------|---------|--------|-------|
| D1 | Completed penetration test | Security team | Jun 18 | Not started — confirm date | Security lead |

---

Notice what the skill did: sorted each concern into the right RAID category, scored the risks for severity, gave Critical/High risks both a mitigation *and* a contingency, flagged the unconfirmed assumption with what happens if it's wrong, and pulled the vital few into a "Top items" summary for the review.
