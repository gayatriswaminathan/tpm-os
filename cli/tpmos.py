#!/usr/bin/env python3
"""
tpmos — a tiny, model-agnostic CLI that runs TPM OS skills against your
program data.

It pulls data through source adapters (Jira / metrics / Confluence — here over
bundled synthetic sample data), loads a skill's instructions, and asks whatever
LLM you have configured to produce the artifact. Works offline with no API key.

Examples:
    python tpmos.py list
    python tpmos.py summarize --skill status-update --audience exec
    python tpmos.py summarize --skill risk-tracker --source sample_data
"""

import argparse
import json
import sys
from pathlib import Path

from adapters import gather_context
from providers import get_provider
from skills import list_skills, load_skill

HERE = Path(__file__).resolve().parent


def build_user_prompt(context: dict, audience: str) -> str:
    """Turn the normalized context into the user message for the skill."""
    jira = context["jira"]
    metrics = context["metrics"]
    lines = [
        f"audience: {audience}",
        f"program: {jira['program']}",
        f"sprint: {jira.get('sprint', 'n/a')}",
        f"milestones: {metrics['milestones']['complete']} of {metrics['milestones']['total']} complete",
        f"issues: {jira['issues_done']} of {jira['issues_total']} done "
        f"({jira['points_done']}/{jira['points_total']} points)",
        f"status breakdown: {json.dumps(jira['counts'])}",
        f"incidents this week: {metrics.get('incidents_this_week', 0)}",
        "",
        "blocked items:",
    ]
    for b in jira["blocked"]:
        lines.append(f"  - {b['key']} {b['summary']} (owner: {b['owner']})")
    lines.append("")
    lines.append("open risks:")
    for r in metrics.get("open_risks", []):
        lines.append(f"  - [{r['severity']}] {r['risk']} (owner: {r['owner']}, due: {r['due']})")
    lines.append("")
    lines.append("dependencies:")
    for d in metrics.get("dependencies", []):
        lines.append(f"  - need {d['need']} from {d['from']} by {d['by']} ({d['status']})")
    lines.append("")
    lines.append("working notes:")
    lines.append(context["notes"])
    return "\n".join(lines)


def cmd_list(args):
    skills = list_skills()
    if not skills:
        print("No skills found.")
        return
    print("Available skills:")
    for s in skills:
        print(f"  - {s}")


def cmd_summarize(args):
    source = (HERE / args.source) if not Path(args.source).is_absolute() else Path(args.source)
    if not source.exists():
        sys.exit(f"Source folder not found: {source}")

    context = gather_context(source)
    system = load_skill(args.skill)
    user = build_user_prompt(context, args.audience)

    provider = get_provider()
    print(f"[tpmos] skill={args.skill} audience={args.audience} provider={provider.name}\n")
    output = provider.complete(system, user)
    print(output)


def main():
    parser = argparse.ArgumentParser(
        prog="tpmos", description="Run TPM OS skills against your program data."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List available skills")
    p_list.set_defaults(func=cmd_list)

    p_sum = sub.add_parser("summarize", help="Run a skill and print the artifact")
    p_sum.add_argument("--skill", default="status-update", help="Skill name (see `list`)")
    p_sum.add_argument("--audience", default="exec", choices=["exec", "stakeholder", "engineering"])
    p_sum.add_argument("--source", default="sample_data", help="Folder with source data")
    p_sum.set_defaults(func=cmd_summarize)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
