#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """Doc"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
