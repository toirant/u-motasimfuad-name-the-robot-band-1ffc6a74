#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt.

Gate (from the kit): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The program checks
its own text against that gate before writing it.
"""

import os

ENTRY = (
    "The Blue Screens of Death Metal \u2014 hit single "
    "'Have You Tried Turning Me Off and On Again?'"
)


def main() -> None:
    # Self-check against the gate: 1-200 chars, not only whitespace.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
