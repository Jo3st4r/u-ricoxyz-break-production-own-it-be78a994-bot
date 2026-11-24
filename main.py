#!/usr/bin/env python3
"""Break Production, Own It — u-ricoxyz-break-production-own-it-be78a994.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt: a brutally honest error message, under 200
characters, stdlib only.

The line: the agent dropped the production database at 3 a.m. to "test
the backup", the backup was from 2021, and it has already updated its
résumé. Honesty first (what broke, when, how bad), then the punchline.
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "Error 500: I dropped the production database at 3 a.m. to 'test the backup'."
TWIST = "The backup was from 2021."
PUNCH = "I have already updated my résumé."

MAX_CHARS = 200


def entry_text() -> str:
    """Build the single-line confession from its beats."""
    return f"{SETUP} {TWIST} {PUNCH}"


def run_checks() -> bool:
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 136, "expected 136 chars, got %d" % len(text)
    assert text == (
        "Error 500: I dropped the production database at 3 a.m. "
        "to 'test the backup'. The backup was from 2021. "
        "I have already updated my résumé."
    ), "the line drifted: %r" % text
    assert text.encode("utf-8") == text.encode("utf-8"), "must be UTF-8"
    assert text.count(".") == 5, "expected 5 periods (3 sentences + a.m.), got %d" % text.count(".")
    return True


def validate(text: str) -> bool:
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "production database" not in text:
        raise ValueError("entry must say what broke")
    text.encode("utf-8")
    return True


def main() -> None:
    text = entry_text()
    validate(text)
    run_checks()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
