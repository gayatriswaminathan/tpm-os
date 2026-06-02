# tpmos — the TPM OS CLI

A tiny, **model-agnostic** command-line tool that runs TPM OS skills against your
program data and prints the finished artifact.

It demonstrates the full pipeline a real TPM automation needs:

```
source adapters  →  normalized context  →  skill instructions  →  LLM  →  artifact
 (Jira / metrics /     (one dict)            (SKILL.md)         (any)    (exec email)
  Confluence)
```

The adapters here read **bundled synthetic sample data**, so it runs for anyone
with no credentials and no real systems. Swapping to live Jira / Confluence /
SharePoint (via their APIs or an MCP server) is a one-file change in
[`adapters.py`](adapters.py) — the rest of the pipeline is untouched.

## Run it in 30 seconds

No API key or dependencies required — it falls back to an offline mode that
renders directly from the structured data:

```bash
cd cli
python tpmos.py list
python tpmos.py summarize --skill status-update --audience exec
```

## Generate a real, LLM-written summary

Install your provider of choice and set its key — `tpmos` detects it
automatically:

```bash
pip install anthropic          # or: pip install openai
export ANTHROPIC_API_KEY=...    # or: export OPENAI_API_KEY=...
python tpmos.py summarize --skill status-update --audience exec
```

## Commands

| Command | What it does |
|---|---|
| `tpmos list` | List the available skills |
| `tpmos summarize --skill <name> --audience <exec\|stakeholder\|engineering> --source <dir>` | Run a skill against the source data and print the artifact |

## How it's built

- **`tpmos.py`** — the CLI (argparse). Assembles the prompt and prints the result.
- **`adapters.py`** — `JiraAdapter`, `MetricsAdapter`, `ConfluenceAdapter`. Each
  normalizes one source into a plain dict. Point them at real APIs to go live.
- **`providers.py`** — model-agnostic LLM layer. Resolves Anthropic → OpenAI →
  offline, so the same code runs with any provider or none.
- **`skills.py`** — loads a skill's `SKILL.md` from [`../skills/`](../skills) and
  uses its instructions as the system prompt.
- **`sample_data/`** — a synthetic program ("Payments Migration") to run against.

## Design notes

- **Model-agnostic by construction.** The CLI never imports a vendor SDK directly;
  it asks `get_provider()` for whatever is configured.
- **Skills are the single source of truth.** The CLI doesn't hard-code prompts —
  it reads the same `SKILL.md` files a human would use in Claude or Copilot.
- **Runnable by default.** Offline mode guarantees a result on first clone, so the
  tool is never a dead demo.
