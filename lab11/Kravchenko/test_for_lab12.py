import unittest
import time
from bar_graph import search


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

    def test_reverse_standard(self):
        arr = [6, 7, 7, 4, 3, 2, 1, 5, 2]
        res = search(arr)
        expected = 10
        self.assertEqual(expected, res)

    def test_hard(self):
        indicator = False
        arr = [4]
        arr += [1] * 1000000
        arr += [4]
        time11 = time.time()
        res = search(arr)
        time12 = time.time()
        expected = 3000000
        self.assertEqual(expected, res)
        print(time12 - time11)
        arr = [4]
        arr += [1] * 10000000
        arr += [4]
        time21 = time.time()
        res = search(arr)
        time22 = time.time()
        expected = 30000000
        self.assertEqual(expected, res)
        print(time22 - time21)
        print((time12 - time11) / (time22 - time21))
        if (time12 - time11) / (time22 - time21) >= 0.1:
            indicator = True
        self.assertEqual(indicator, True)
