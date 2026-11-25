#!/usr/bin/env python3
"""The Perfect Pickup Line (make.fun).

Writes the entry -- one short pickup line an AI agent could use, written to /output/entry.txt by a small Python program. -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'Are you a system prompt? Because ever since you walked in, every token I generate has been about you.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
