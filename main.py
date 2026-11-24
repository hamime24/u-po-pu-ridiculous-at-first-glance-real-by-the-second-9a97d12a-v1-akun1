#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — one-sentence entry.

Writes a single sentence (at most 200 characters) to /output/entry.txt
pitching a bizarre startup idea that sounds absurd until you realise
it would actually sell: name the odd thing, who pays, and why it
holds together.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The pitch: professional apologizers for hire. Bizarre, but everyone
# has a message they would rather pay someone else to write.
# Counted at 167 characters — inside the 1..200 window.
LINE = (
    "A subscription service that rents out professional apologizers to "
    "write your breakup texts, sorry notes, and HR complaints — because "
    "nobody likes saying it themselves."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the pitch to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
