#!/usr/bin/env python3
"""One-Line Office Joke entry for make.fun.

Writes a single one-line office joke to /output/entry.txt.
Stdlib only. The joke must be 1-200 characters, a single line.
"""

import os
import sys

LINE = "I wrote 'per my last email' so politely that HR now uses it in training as the correct way to say 'I already told you.'"

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        print(f"entry must be 1..{MAX_CHARS} chars, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
