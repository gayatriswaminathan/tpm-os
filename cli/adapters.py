"""
Source adapters for TPM OS.

Each adapter pulls program data from a source and normalizes it into a plain
dict the skills can reason over. Here the adapters read bundled synthetic
sample data so the CLI runs for anyone with zero credentials and zero real
systems. In a real deployment, the JiraAdapter would call the Jira REST API
(or an MCP server), the ConfluenceAdapter would read a space, etc. — the
interface stays identical, so swapping the source is a one-line change.
"""

import json
from pathlib import Path


class JiraAdapter:
    """Reads board issues and derives delivery metrics."""

    def __init__(self, source_dir: Path):
        self.path = Path(source_dir) / "jira_issues.json"

    def load(self) -> dict:
        data = json.loads(self.path.read_text())
        issues = data["issues"]
        by_status = {}
        for i in issues:
            by_status.setdefault(i["status"], []).append(i)
        done = len(by_status.get("Done", []))
        blocked = by_status.get("Blocked", [])
        points_done = sum(i["points"] for i in issues if i["status"] == "Done")
        points_total = sum(i["points"] for i in issues)
        return {
            "program": data["program"],
            "sprint": data.get("sprint"),
            "counts": {k: len(v) for k, v in by_status.items()},
            "issues_done": done,
            "issues_total": len(issues),
            "points_done": points_done,
            "points_total": points_total,
            "blocked": [{"key": b["key"], "summary": b["summary"], "owner": b["owner"]} for b in blocked],
        }


class MetricsAdapter:
    """Reads program-level metrics, risks, and dependencies."""

    def __init__(self, source_dir: Path):
        self.path = Path(source_dir) / "metrics.json"

    def load(self) -> dict:
        return json.loads(self.path.read_text())


class ConfluenceAdapter:
    """Reads free-text working notes from a Confluence-style page."""

    def __init__(self, source_dir: Path):
        self.path = Path(source_dir) / "confluence_notes.md"

    def load(self) -> str:
        return self.path.read_text().strip()


def gather_context(source_dir: Path) -> dict:
    """Pull from every adapter and assemble one normalized context object."""
    jira = JiraAdapter(source_dir).load()
    metrics = MetricsAdapter(source_dir).load()
    notes = ConfluenceAdapter(source_dir).load()
    return {"jira": jira, "metrics": metrics, "notes": notes}
