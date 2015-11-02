__author__ = 'alexkane'

import unittest
import lab11

class TestHistogram(unittest.TestCase):

    def test_from_boss(self):
        input = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        expected = 10
        res = lab11.execute(input)
        self.assertEqual(expected, res)

    def test_from_me(self):
        input = [10, 3, 7, 1, 11, 1, 1, 1]
        expected = 19
        res = lab11.execute(input)
        self.assertEqual(expected, res)

    def test_from_me_again(self):
        input = [10, 3, 7, 1, 11, 0, 0, 10]
        expected = 20
        res = lab11.execute(input)
        self.assertEqual(expected, res)