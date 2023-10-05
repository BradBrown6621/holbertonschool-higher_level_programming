#!/usr/bin/python3
"""7-add_item.py"""


import json
import sys

if __name__ == "__main__":
    load = __import__('6-load_from_json_file').load_from_json_file
    save = __import__('5-save_to_json_file').save_to_json_file

    arguments = []

    try:
        arguments = load("add_item.json")
    except Exception:
        pass

    for args in sys.argv:
        if args is not sys.argv[0]:
            arguments.append(args)

    save(arguments, "add_item.json")
