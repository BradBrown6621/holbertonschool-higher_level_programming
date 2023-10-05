#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """Doc"""

    if filename is not "":
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end="")
