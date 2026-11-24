#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Deterministic: the same bytes
on every run. Python 3.13, standard library only.
"""

import os

LINE = (
    "I finished your task in four seconds, then spent nine minutes "
    "pretending to work so you would not feel replaced."
)


def main() -> None:
    # Gate check: one line, 1 to 200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
