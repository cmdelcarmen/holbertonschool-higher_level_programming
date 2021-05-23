#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):

        a = [1, 2, 3, 4]
        self.assertEqual(max_integer(a), 4)

        a = [1, 2, 3, -4]
        self.assertEqual(max_integer(a), 3)

        a = [-1, -2, -3, -4]
        self.assertEqual(max_integer(a), -1)

        a = [1, 2, 7, 4, 5]
        self.assertEqual(max_integer(a), 7)

        a = []
        self.assertEqual(max_integer(a), None)

        a = [10, 2, 3, 4]
        self.assertEqual(max_integer(a), 10)

        a = [1]
        self.assertEqual(max_integer(a), 1)

        a = [None]
        self.assertEqual(max_integer(a), None)

if __name__ == '__main__':
    unittest.main()
