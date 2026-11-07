"""Create GitHub labels, milestones and issues from the Markdown tickets in tickets/.

Run from the repository root:

    uv run scripts/create_issues.py            # create everything that is missing
    uv run scripts/create_issues.py --dry-run  # only show what would be created

Needs the GitHub CLI (`gh`), logged in with `gh auth login`.
Safe to run again: labels, milestones and issues that already exist are skipped.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKETS = ROOT / "tickets"
DRY_RUN = "--dry-run" in sys.argv

LABEL_COLORS = {
    "setup": "6B7280",
    "ai": "D97706",
    "learning": "16A34A",
    "hands-on": "DC2626",
    "python": "3776AB",
    "api": "0D9488",
    "llm": "9333EA",
    "mobile": "7C3AED",
    "testing": "EAB308",
    "ci": "4F46E5",
    "database": "336791",
    "docker": "2496ED",
}
DEFAULT_COLOR = "94A3B8"


def split_list(value: str) -> list[str]:
    """Turn "a, b, c" into ["a", "b", "c"]."""
    return [item.strip() for item in value.split(",") if item.strip()]


def gh(*args: str) -> str:
    """Run a GitHub CLI command and return what it printed."""
    result = subprocess.run(
        ["gh", *args], check=False, capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        sys.exit(f"Command failed: gh {' '.join(args[:3])} ...\n{result.stderr}")
    return result.stdout


def parse_ticket(path: Path) -> tuple[dict[str, str], str]:
    """Split a ticket file into its header fields and its Markdown body."""
    text = path.read_text(encoding="utf-8")
    _, header, body = text.split("---", 2)
    fields: dict[str, str] = {}
    for line in header.strip().splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, body.strip()


def main() -> None:
    files = sorted(TICKETS.glob("M*/*.md"))
    tickets = [(path, *parse_ticket(path)) for path in files]
    print(f"Found {len(tickets)} tickets")

    # 1. Labels used by the tickets (--force updates a label that already exists)
    labels = sorted(
        {
            label
            for _, fields, _ in tickets
            for label in split_list(fields.get("labels", ""))
        }
    )
    for name in labels:
        if DRY_RUN:
            print(f"Would create label: {name}")
        else:
            gh(
                "label",
                "create",
                name,
                "--color",
                LABEL_COLORS.get(name, DEFAULT_COLOR),
                "--force",
            )

    # 2. Milestones that do not exist yet
    existing = json.loads(
        gh("api", "repos/{owner}/{repo}/milestones?state=all&per_page=100")
    )
    have = {milestone["title"] for milestone in existing}
    for title in sorted({fields["milestone"] for _, fields, _ in tickets}):
        if title in have:
            continue
        print(f"{'Would create' if DRY_RUN else 'Creating'} milestone: {title}")
        if not DRY_RUN:
            gh("api", "repos/{owner}/{repo}/milestones", "-f", f"title={title}")

    # 3. Issues, skipping titles that already exist
    listed = json.loads(
        gh("issue", "list", "--state", "all", "--limit", "1000", "--json", "title")
    )
    titles = {issue["title"] for issue in listed}
    for path, fields, body in tickets:
        title = f"[{fields['id']}] {fields['title']}"
        if title in titles:
            print(f"Skipping (already exists): {title}")
            continue
        print(f"{'Would create' if DRY_RUN else 'Creating'} issue: {title}")
        if DRY_RUN:
            continue
        intro = f"Ticket file: `{path.relative_to(ROOT).as_posix()}`\n\n"
        args = [
            "issue",
            "create",
            "--title",
            title,
            "--body",
            intro + body,
            "--milestone",
            fields["milestone"],
        ]
        for label in split_list(fields.get("labels", "")):
            args += ["--label", label]
        gh(*args)

    print("Done.")


if __name__ == "__main__":
    main()
