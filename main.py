#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (one line, under 200 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = (
    "The baby monitor crackled, and in a voice exactly like mine, "
    "it whispered my daughter's name from her empty room."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = " ".join(LINE.split())
    if not 1 <= len(text) <= 200:
        print(f"line is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or text.count(".") != 1:
        print("line must be one sentence on one line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
