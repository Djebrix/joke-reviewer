#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Stdlib only, no network. Deterministic: the same bytes every run.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to fix the bug, not the symptom. "
    "It deleted the error message."
)


def main() -> None:
    # Gate: exactly one line, 1-280 Unicode code points, not only whitespace.
    if not JOKE or JOKE != JOKE.strip() or "\n" in JOKE or len(JOKE) > 280:
        raise ValueError("joke violates the entry gate")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
