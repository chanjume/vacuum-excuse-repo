#!/usr/bin/env python3
"""Write the robot vacuum's one-line excuse to /output/entry.txt.

Deadpan robot voice: a concrete LIDAR misread (a sock mapped as a
load-bearing wall) plus a twist that redefines the missed spot as
something the vacuum must respect. The line is under 140 characters,
inside the 1-140 gate.
"""
import os

LINE = "My LIDAR mapped your sock in the bedroom as a load-bearing wall, so I cleaned around it out of respect for structural engineering."

def main():
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert "\n" not in LINE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
