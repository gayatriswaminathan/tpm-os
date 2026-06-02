"""
Skill loader for TPM OS.

A skill lives at ../skills/<name>/SKILL.md with YAML frontmatter (name,
description) followed by the instruction body. This reads the file, splits off
the frontmatter, and returns the instruction body to use as the system prompt.
"""

from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


def list_skills() -> list[str]:
    if not SKILLS_DIR.exists():
        return []
    return sorted(p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())


def load_skill(name: str) -> str:
    skill_path = SKILLS_DIR / name / "SKILL.md"
    if not skill_path.exists():
        raise FileNotFoundError(
            f"Skill '{name}' not found. Available: {', '.join(list_skills()) or 'none'}"
        )
    text = skill_path.read_text()
    # Strip leading YAML frontmatter delimited by --- ... ---
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()
