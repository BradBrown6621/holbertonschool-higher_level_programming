#!/usr/bin/python3
"""6-load_from_json_file.py"""


import json


def load_from_json_file(filename):
    """Loads new object from JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
