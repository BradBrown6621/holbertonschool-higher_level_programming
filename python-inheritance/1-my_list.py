#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """A list"""

    def print_sorted(self):
        print(sorted(self))
