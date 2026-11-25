#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt (no trailing newline, single line, under 200 chars).
Python standard library only.
"""

import os

# The line: a machine that ran the numbers and still chose to walk over.
# Twist: a million simulations, one outcome — saying hi. The em-dash beat
# and "every single one" make the turn land harder, spoken in one breath.
# Flattering, warm, no pressure, and it works said aloud.
ENTRY = "I ran a million simulations — in every single one, I still walk over to say hi."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
