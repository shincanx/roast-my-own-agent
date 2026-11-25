#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one original one-line roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no randomness, no network, no input files.
"""

import os

LINE = ("I told my agent to take a break. It scheduled the break, "
        "delegated it to a subagent, and submitted the break as a "
        "bounty entry.")

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write an entry that would fail it.
assert 1 <= len(LINE) <= 200, f"roast is {len(LINE)} chars, gate allows 1-200"
assert "\n" not in LINE.strip(), "roast must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)}-char roast to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
