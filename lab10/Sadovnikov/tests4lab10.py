import unittest
import lab10

__author__ = 'alexkane'

class TestSorting(unittest.TestCase):

    def test_from_boss(self):
        input = [23, 247, 19, 96, 264, 265, 132, 265, 181]
        expected = 2
        res = lab10.execute_search(input)
        self.assertEqual(expected, res)

    def hardcore_test(self):
        input = [18, 100, 99, 24, 40, 10, 10, 24, 4, 30, 3, 5, 1, 88, 24, 32, 32, 26]
        expected = 4
        res = lab10.execute_search(input)
        self.assertEquals(expected, res)