<h1 align="center">TPM OS</h1>

<p align="center"><b>Open-source AI skills for the technical program manager's craft.</b></p>

<p align="center">Clone, customize, run — turn the repetitive parts of program management into reusable AI skills.</p>

---

## What this is

TPM OS is a growing library of AI **skills** that automate the work technical program managers do every week — status reporting, risk and dependency tracking, launch readiness, governance, and stakeholder communication.

Each skill is a self-contained, model-agnostic instruction set. Drop it into [Claude](https://claude.com), GitHub Copilot, or any assistant that supports skills or [MCP](https://modelcontextprotocol.io), point it at your own inputs, and get a polished, consistent output in seconds instead of an hour.

Built by a working TPM, for working TPMs. No fluff, no vendor lock-in.

## Why

Program management runs on the same artifacts produced over and over: the weekly exec update, the RAID log, the dependency map, the launch checklist. They're high-leverage but tedious, and quality drifts when you're busy. TPM OS captures the *structure* of each artifact once, so the thinking stays yours and the busywork goes away.

## Skill catalog

**Delivery & communication**

| Skill | What it does | Status |
|---|---|---|
| 🟢 **status-update** | Turns raw notes into a clean exec / stakeholder status update | Available |
| 🟢 **risk-tracker** | Builds and maintains a RAID log (Risks, Assumptions, Issues, Dependencies) | Available |
| ⚪ **release-notes-pro** | Generates polished release notes from a changelog or ticket list | Planned |
| ⚪ **incident-postmortem** | Drafts a blameless postmortem from an incident timeline | Planned |
| ⚪ **meeting-orchestrator** | Builds agendas, captures decisions, and assigns action items | Planned |

**Strategy & planning**

| Skill | What it does | Status |
|---|---|---|
| 🟢 **prd-generator** | Turns a feature idea into a structured PRD with goals and acceptance criteria | Available |
| ⚪ **roadmap-builder** | Builds a Now / Next / Later roadmap from initiatives and priorities | Planned |
| ⚪ **prioritization-engine** | Scores and ranks a backlog against a chosen framework (RICE, WSJF) | Planned |
| ⚪ **okr-coach** | Drafts and pressure-tests OKRs for clarity and measurability | Planned |
| ⚪ **north-star-finder** | Helps define a north-star metric and its input drivers | Planned |
| ⚪ **gtm-strategy** | Structures a go-to-market plan for a launch | Planned |
| ⚪ **portfolio-visualizer** | Summarizes a portfolio's health, status, and dependencies | Planned |

*New skills ship regularly. Suggestions welcome — open an issue.*

## Getting started

1. Browse [`skills/`](skills/) and pick a skill.
2. Open its `SKILL.md` to see what it does and what inputs it expects.
3. Copy the skill into your AI assistant (Claude Skills, a custom instruction, or an MCP server) and run it against your own data.
4. Check the `examples/` folder in each skill to see the expected output.

## Structure

```
tpm-os/
├── README.md
└── skills/
    ├── status-update/
    │   ├── SKILL.md
    │   └── examples/weekly-status-example.md
    ├── prd-generator/
    │   ├── SKILL.md
    │   └── examples/prd-example.md
    └── risk-tracker/
        ├── SKILL.md
        └── examples/raid-log-example.md
```

## Author

Built and maintained by [Gayatri Swaminathan](https://github.com/gayatriswaminathan).
