#!/usr/bin/env python3
"""Write the funniest AI excuse line to /output/entry.txt."""

import os

TEXT = "I asked myself for a second opinion, and we have been in a meeting about it ever since. The minutes are excellent. The task is not in them."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
