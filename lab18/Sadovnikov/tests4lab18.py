__author__ = 'alexkane'

import lab18
import unittest

class TestLevi(unittest.TestCase):
    def test_from_boss(self):
        res = lab18.execute("Levenshtien", "Frankenstein")
        expected = 7
        self.assertEqual(expected, res)

    def test_from_me(self):
        res = lab18.execute("one", "two")
        expected = 3
        self.assertEqual(expected, res)

    def test_trivial(self):
        res = lab18.execute("1", "2")
        expected = 1
        self.assertEqual(expected, res)

