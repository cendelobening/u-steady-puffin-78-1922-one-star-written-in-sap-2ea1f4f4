#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review by a houseplant about its human
owner to /output/entry.txt.
"""
import os

LINE = "One star: he repotted me into a pot with no drainage holes, then looked betrayed when I started swimming \u2014 I'm a fern, not a goldfish, and nobody asked for a pool."

assert 1 <= len(LINE) <= 279, len(LINE)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
