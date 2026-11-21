#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Stdlib only, no network. Deterministic: the same bytes every run.
"""

from pathlib import Path

JOKE = (
    "My AI coding agent writes the code, reviews its own pull request, "
    "approves it in seconds \u2014 and I'm still the one explaining "
    "the bug at standup."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
