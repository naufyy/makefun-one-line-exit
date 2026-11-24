#!/usr/bin/env python3
"""The One-Line Exit: one funny single-line resignation letter.
Writes the letter to /output/entry.txt.

The letter is a single line of 108 characters: a concrete workplace
scene (the homemade spreadsheet that replaced its author) with the
punchline landing on the parking space, in a voice a colleague would
forward.
"""
import os

LETTER = "I resign. My replacement is the spreadsheet I built to do my job; it has already asked for my parking space."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")

if __name__ == "__main__":
    main()
