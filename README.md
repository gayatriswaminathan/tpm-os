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
| 🟢 **drift-detector** | Spots program drift — the gap between effort and progress — before a program is formally at risk | Available |
| ⚪ **release-notes-pro** | Generates polished release notes from a changelog or ticket list | Planned |
| ⚪ **incident-postmortem** | Drafts a blameless postmortem from an incident timeline | Planned |
| ⚪ **meeting-orchestrator** | Builds agendas, captures decisions, and assigns action items | Planned |

**Strategy & planning**

| Skill | What it does | Status |
|---|---|---|
| 🟢 **prd-generator** | Turns a feature idea into a structured PRD with goals and acceptance criteria | Available |
| 🟢 **roadmap-builder** | Builds a Now / Next / Later roadmap from initiatives and priorities | Available |
| ⚪ **prioritization-engine** | Scores and ranks a backlog against a chosen framework (RICE, WSJF) | Planned |
| ⚪ **okr-coach** | Drafts and pressure-tests OKRs for clarity and measurability | Planned |
| ⚪ **north-star-finder** | Helps define a north-star metric and its input drivers | Planned |
| ⚪ **gtm-strategy** | Structures a go-to-market plan for a launch | Planned |
| ⚪ **portfolio-visualizer** | Summarizes a portfolio's health, status, and dependencies | Planned |

*New skills ship regularly. Suggestions welcome — open an issue.*

## Two ways to use it

**1. Drop a skill into your assistant.** Browse [`skills/`](skills/), open a `SKILL.md`, and paste it into Claude, Copilot, or an MCP server. Run it against your own data, and check each skill's `examples/` folder for the expected output.

**2. Run the CLI.** [`cli/`](cli/) ships a tiny, **model-agnostic** Python tool — `tpmos` — that pulls program data through source adapters (Jira / metrics / Confluence) and runs a skill to produce the artifact. Works offline with no API key:

```bash
cd cli
python tpmos.py list
python tpmos.py summarize --skill status-update --audience exec
```

Set `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` for fully LLM-written output. See [`cli/README.md`](cli/README.md) for details.

## Structure

```
tpm-os/
├── README.md
├── index.html              # landing page (GitHub Pages)
├── cli/                    # runnable, model-agnostic CLI
│   ├── tpmos.py
│   ├── adapters.py         # Jira / metrics / Confluence sources
│   ├── providers.py        # Anthropic / OpenAI / offline
│   ├── skills.py
│   └── sample_data/
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
