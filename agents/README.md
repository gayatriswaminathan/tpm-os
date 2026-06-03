# TPM OS — Agents

Runnable AI agents for the technical program manager's craft. Each agent is a **self-contained app** in its own folder — clone, install, run. They're the TPM OS skills wrapped in real interfaces.

| Agent | What it does | Stack | Status |
|---|---|---|---|
| 📊 [program-status-agent](program-status-agent) | Raw notes → audience-tuned status update | Streamlit + model-agnostic LLM | Live |
| 🛡️ raid-agent | Describe a program → a scored RAID log | _planned_ | Soon |
| 📝 meeting-to-actions | Meeting notes → decisions + action items | _planned_ | Soon |

## Convention

Each agent folder is independently runnable and contains:

```
agents/<agent-name>/
├── app.py            # the agent (Streamlit or CLI)
├── requirements.txt
└── README.md         # what it does + how to run
```

Agents are model-agnostic (Claude / OpenAI / offline) and load their behavior from the shared [`skills/`](../skills) so the agent and a human use one source of truth.
