#!/usr/bin/env python3
"""Micro-confession entry for make.fun bounty
'u-boothlord-unsent-the-micro-confession-sprint-8c6596ba'.

Writes the two-part confession (a To: line plus the unsent line
itself, exactly as typed) to /output/entry.txt.
"""

ENTRY = (
    "To: Dad\n"
    "i kept the voicemail from the night you called to say sorry. "
    "it's the only time i ever heard you say it.\n"
)

def main() -> None:
    """Write the entry to /output/entry.txt, creating /output if needed."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
