#!/usr/bin/env python3
"""One-line review of the most boring everyday object.

Entry for the make.fun bounty "The Most Boring Object, Reviewed in
One Line": the program writes exactly one line of at most 200
characters to /output/entry.txt.

Chosen object: the rubber band. It is the dullest thing on any desk:
no moving parts, no purpose beyond holding other things together,
invisible until the single moment it fails. The joke is built from
that truth -- a lifetime of quiet, faithful service, repaid with one
sting on the wrist in the middle of a meeting. The turn lands early
("retirement plan") and the last words sharpen it.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
LIMIT = 200

# The review is composed from its two beats so each half can be
# checked on its own: the setup (loyal service) and the punch
# (the snap). Joining with a single space keeps it one line.
SETUP = "Six years of faithful service, and the rubber band's"
PUNCH = "retirement plan was snapping my wrist in a meeting."


def compose_review() -> str:
    """Assemble the single-line review from its two beats."""
    parts = [SETUP.strip(), PUNCH.strip()]
    return " ".join(part for part in parts if part)


def validate(line: str) -> str:
    """Enforce the gate: one non-blank line, 1..200 characters."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    return line


def write_entry(path: Path = OUTPUT_PATH) -> str:
    line = validate(compose_review())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    return line


if __name__ == "__main__":
    write_entry()
