# Example: weekly executive status

This shows the `status-update` skill turning raw notes into an exec-ready update.

## Input (raw notes)

```
audience: exec (CIO)
program: Unified Intake Platform
week: ending May 29

notes:
- finished onboarding 3 more teams, now 12 of 18 migrated
- API latency issue last tues, fixed wed, root caused to a config
- still waiting on security sign-off for the SSO piece, blocking go-live
- vendor for the routing engine slipped their delivery by a week
- demo to business stakeholders went well, good feedback
- next: finish remaining 6 team migrations, get security sign-off
```

## Output (generated update)

---

**Unified Intake Platform — Status Update | Week ending May 29**
**Overall: 🟡 Amber — On track on migration, but security sign-off is now the critical-path blocker to go-live.**

**✅ Progress this period**

- Onboarded 3 more teams — **12 of 18 migrated (67%)**, on pace for full migration.
- Stakeholder demo landed well; business confirmed the routing flow meets their needs.
- Resolved a Tuesday API latency incident within 24h (root cause: config; fix deployed Wed).

**🚧 In flight**

- Remaining 6 team migrations underway, targeted to complete next two weeks.

**⚠️ Risks & blockers**

- **Security sign-off for SSO is pending → blocks go-live.** Chasing review; escalating if not cleared by **Jun 3** (owner: G. Swaminathan).
- **Routing-engine vendor slipped delivery by 1 week → risks the integration test window.** Re-sequencing test plan to absorb; will confirm impact by **Jun 2**.

**🙋 Decisions / help needed**

- **Need your help expediting the SSO security review** — a nudge to the security lead would protect the go-live date.

**🔜 Next period**

- Complete remaining migrations, secure SSO sign-off, finalize integration test schedule.

---

Notice what the skill did: led with the headline and the real blocker, gave every Amber item a cause + action + owner + date, separated the one genuine ask from the FYIs, and kept the whole thing to a single screen.
