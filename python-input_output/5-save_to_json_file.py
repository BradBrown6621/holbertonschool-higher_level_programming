#!/usr/bin/python3
"""5-save_to_json_file.py"""


import json


def save_to_json_file(my_obj, filename):
    """Saves Json string representation of object to file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
