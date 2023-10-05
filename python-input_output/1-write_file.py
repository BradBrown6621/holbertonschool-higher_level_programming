#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """Doc"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
