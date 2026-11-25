"""One-liner entry for the make.fun bounty "Monday Morning Punchlines".

Writes the final locked one-liner (128 characters) to /output/entry.txt.

The text is a single line: no embedded newline, no leading/trailing
whitespace, and it must round-trip byte-for-byte through UTF-8.
"""

from pathlib import Path

TEXT = "Monday morning: my laptop asked for a password, my coffee asked for a break, and my calendar asked why I was crying before 9 AM."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = TEXT
    # Gate: text must be non-blank and 1-200 UTF-8 characters.
    assert text.strip(), "entry text must not be blank"
    assert text == text.strip(), "entry text must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry text length {len(text)} out of range 1-200"
    # Extra gate: UTF-8 byte length must stay within the same 200-byte budget
    # the bounty counts in characters; a multibyte surprise must not slip in.
    assert len(text.encode("utf-8")) <= 200, "entry exceeds 200 UTF-8 bytes"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Assert round-trip: what we read back must equal what we wrote.
    assert OUTPUT_PATH.read_text(encoding="utf-8") == text, "round-trip mismatch"
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
