#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_maxintend(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_maxintstart(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_maxinthemiddle(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_negatives(self):
        self.assertEqual(max_integer([3, 2, -1]), 3)

    def test_morenegatives(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_singleton(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
