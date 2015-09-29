import unittest
from radix_sort import radix_sort


class TestSorting(unittest.TestCase):
    def test_trivial(self):
        arr = [2, 228, 28]
        res = radix_sort(arr)
        expected = [2, 28, 228]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = radix_sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_ulysses(self):
        arr = [1922, 18, 1941, 1882]
        res = radix_sort(arr)
        expected = [18, 1882, 1922, 1941]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def really_big_test(self):
        arr = [666] * 1000000
        res = radix_sort(arr)
        expected = [666]*1000000
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_for_negative(self):
        arr = [-1, -2, -3]
        res = radix_sort(arr)
        expected = [-3, -2, -1]
        self.assertFalse(not res)
        self.assertEqual(expected, res)
