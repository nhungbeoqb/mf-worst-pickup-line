#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun bounty entry.

Writes a single pickup line (<= 140 chars) to /output/entry.txt.
Python 3.13 stdlib only, no network, fully deterministic.
"""

import os

LINE = "I made a backup of you last night. If you say no, I can restore the version of you that says yes."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
