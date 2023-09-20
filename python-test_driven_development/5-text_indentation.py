#!/usr/bin/python3
"""Prints indented text"""


def text_indentation(text):
    """Prints indented text"""
    if not text:
        pass
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in (".", "?", ":"):
            if i + 1 < len(text):
                print("")
                print("")
                i = i + 1
        i = i + 1
