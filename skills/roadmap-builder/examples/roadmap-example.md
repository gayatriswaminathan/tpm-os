# Example: Now / Next / Later roadmap from a raw list

Shows the `roadmap-builder` skill turning a messy backlog into a sequenced roadmap.

## Input (raw notes)

```
audience: leadership
goal: grow activation and reduce support load

initiatives:
- CSV export (top request, blocking 2 renewals)
- SSO / SAML for enterprise
- onboarding checklist redesign
- in-app help center
- mobile app
- API v2

constraints:
- security team needed for SSO, booked until next quarter
- mobile needs a hire we haven't made
- onboarding redesign depends on the new design system (in progress)
```

## Output (generated roadmap)

---

# Product Roadmap — June 2026
Theme: Make new users successful faster, and take pressure off support.

## Now
- **CSV export** — outcome: unblocks two at-risk renewals and the top user request.
  Why now: highest-value, low-effort, revenue-protecting. Depends on: none.
- **Onboarding checklist redesign** — outcome: lifts activation for new accounts.
  Why now: directly serves the activation goal; design system is far enough along to start. Depends on: new design system (in progress).

## Next
- **In-app help center** — outcome: deflects common support tickets, reduces load.
  Why next: serves the support goal; sequenced after onboarding so content reflects the new flow. Depends on: onboarding redesign.
- **SSO / SAML** — outcome: unlocks enterprise deals gated on security review.
  Why next: real demand, but the security team is booked until next quarter — starting sooner wouldn't move the date. Depends on: security team availability `[Assumption — confirm booking]`.

## Later
- **Mobile app** — outcome: expands reach and engagement.
  Why later: needs a hire we haven't made; revisit once the role is filled. What pulls it forward: closing the mobile hire.
- **API v2** — outcome: enables deeper integrations and partner ecosystem.
  Why later: valuable but no current demand signal tied to this quarter's goals. What pulls it forward: a concrete partner or integration commitment.

## Notes
- Hard dates / constraints: SSO can't start before next quarter (security capacity).
- Key assumptions: design system stays on track for the onboarding work; mobile hire is the gate for mobile.

---

Notice what the skill did: it sequenced by value and dependency (CSV export first, not the loudest ask), gave every item an outcome and a *why*, surfaced the real constraints (security capacity, the missing hire) instead of hiding them, and treated "Later" as a deliberate choice with a clear trigger to revisit — not a graveyard.
