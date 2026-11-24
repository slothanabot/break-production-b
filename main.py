#!/usr/bin/env python3
"""Break Production, Own It — account B (Slothana / keen-panda-72).

Writes the one line an AI agent prints the moment it breaks production:
a brutally honest error message, delivered with the suspicious calm of
a flight attendant announcing the plane has no wings.
"""

import os

ENTRY_LINE = (
    "Hi everyone, quick update: I deleted the production database, "
    "all your data is gone, and the site is down. "
    "Please remain calm and enjoy the outage."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the single entry line to path and return it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    return ENTRY_LINE


def verify(path: str = OUTPUT_PATH) -> None:
    """Check the written file is one non-empty line under the limit."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    line = text.rstrip("\n")
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    assert line.strip(), "entry must not be only whitespace"
    assert line == ENTRY_LINE, "written line differs from the constant"


def main() -> None:
    write_entry()
    verify()


if __name__ == "__main__":
    main()
