#!/usr/bin/env python3
"""The funniest one-line resignation letter.

The cron job that has fired every minute since March hands in its notice.
Writes exactly one line (at most 140 characters) to /output/entry.txt.
"""

import os

ENTRY = "I resign, effective immediately. I fired every minute since March, never missed a shift, and nobody once said thank you. Ask the calendar."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
