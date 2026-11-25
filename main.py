"""The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt. Deterministic: the same ten bytes on every run.

The word is "doomscroll": the internet's dominant mode is endless
scrolling through bad news, and the word is funny by itself, true of
the internet as a whole, and short enough to land in one beat.
"""

import os

WORD = "doomscroll"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """The gate allows 1-30 UTF-8 characters, not only white space."""
    encoded = word.encode("utf-8")
    if not 1 <= len(encoded) <= 30:
        raise ValueError("entry must be 1-30 bytes")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    return word


def main() -> None:
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(word.encode("utf-8"))


if __name__ == "__main__":
    main()
