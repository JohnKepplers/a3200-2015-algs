import unittest
import time
from lab12 import search

class TestSorting(unittest.TestCase):
    def test_trivial_one(self):
        arr = [2, 2, 8]
        res = search(arr)
        expected = 0
        self.assertEqual(expected, res)



    def test_trivial_two(self):
        arr = [3, 1, 2, 1, 6]
        res = search(arr)
        expected = 5
        self.assertEqual(expected, res)



    def test_standard(self):
        arr = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        res = search(arr)
        expected = 10
        self.assertEqual(expected, res)


    def test_hard(self):
        arr = [4]
        arr += [1]*10000000
        arr += [4]
        res = search(arr)
        expected = 30000000
        self.assertEqual(expected, res)
        print(time.clock())
