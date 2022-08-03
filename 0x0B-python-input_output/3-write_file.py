#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """Overwrites a file an returns numbers of bytes"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return f.tell()
