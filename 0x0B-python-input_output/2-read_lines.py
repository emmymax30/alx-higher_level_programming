#!/usr/bin/python3
"""Module that read n lines of a file"""


def read_lines(filename="", nb_lines=0):
    """Reading n files of a file"""
    with open(filename, mode="r", encoding='utf-8') as f:
        nLines = sum(1 for line in f)
        f.seek(0)  # Puting the file at the begining
        if nb_lines <= 0 or nb_lines >= nLines:
            print(f.read(), end="")
        else:
            while nb_lines:
                print(f.readline(), end='')
                nb_lines -= 1
