"""A tiny desk-drawer gag generator for a one-line joke contest.

The script picks a single quip about cubicle life and drops it
into /output/entry.txt, where the contest expects to find it.
"""

from pathlib import Path

ENTRY_FILE = Path("/output/entry.txt")


def cubicle_quip():
    """Return one office joke line, freshly made up."""
    return (
        "My out-of-office reply now answers emails faster than I do, "
        "so HR promoted it to my manager."
    )


def confirm_quip_saved(expected):
    """Make sure the file on disk still says what we meant to say."""
    saved = ENTRY_FILE.read_text(encoding="utf-8")
    assert saved == expected


def main():
    quip = cubicle_quip()
    ENTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Save the quip on its own, with no newline at the end.
    ENTRY_FILE.write_text(quip, encoding="utf-8")
    # Reread the file and check it matches the quip exactly.
    confirm_quip_saved(quip)


if __name__ == "__main__":
    main()
