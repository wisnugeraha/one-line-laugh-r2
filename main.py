#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry (round 2).

Writes exactly one funny line to /output/entry.txt.
The program is the entry: a single sentence of at most 200 characters
on any subject, submitted as plain text.
"""
import os


# The entry line: one single sentence, ≤200 chars, a surprise that still
# makes sense, recognisable as an everyday truth, economical.
LINE = "I set a reminder to stop reminding myself that I would stop setting reminders."

# Hard caps set by the gate: 1–200 chars of non-blank UTF-8 text.
MIN_CHARS = 10
MAX_CHARS = 200


def line() -> str:
    """Return the entry line."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line()
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars (max {MAX_CHARS})")
    if len(text) < MIN_CHARS:
        raise ValueError(f"line is {len(text)} chars (min {MIN_CHARS})")
    if not text.strip():
        raise ValueError("line is empty")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Leave the file world-readable: the grader collects it as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
