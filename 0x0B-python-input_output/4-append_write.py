#!/usr/bin/python3
"""Using append mode and writing"""


def append_write(filename="", text=""):
    """Appends content to a file an returns numbers of bytes"""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
