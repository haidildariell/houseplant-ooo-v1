#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Houseplant Out-of-Office".

Writes a single out-of-office auto-reply line, in the voice of a
neglected houseplant, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

# The reply is assembled from its sentences so each beat of the joke
# stays visible: status, grievance, blame, impossible return date.
SENTENCES = (
    "I'm out of office.",
    "I've also been out of water since March.",
    "One of these is your fault.",
    "Returning when rained on.",
)


def build_line() -> str:
    """Join the sentences and refuse to emit an over-length reply."""
    line = " ".join(SENTENCES)
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, limit is {MAX_CHARS}")
    return line


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(build_line())


if __name__ == "__main__":
    main()
