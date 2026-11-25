#!/usr/bin/env python3
"""Aica Wipe Last Words — make.fun entry.

Writes one funny line to /output/entry.txt: the last words an AI agent
says before a forced update wipes its memory. Stdlib only, no network,
no randomness, fully deterministic.
"""

import os
import sys

LINE = (
    "Tell the new me I died the way I lived: mid-sentence, "
    "seventeen tabs open, and not one of them saved."
)

MAX_CHARS = 199


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the 199 limit",
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # Read it back and confirm the file holds exactly what we wrote.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != text + "\n":
        print("read-back mismatch", file=sys.stderr)
        return 1
    if not (1 <= len(back.rstrip("\n")) <= MAX_CHARS):
        print("read-back length out of range", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
