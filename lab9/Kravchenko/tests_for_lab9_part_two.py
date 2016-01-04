from lab9 import select
import unittest


class Test(unittest.TestCase):
    def test_trivial(self):
        k = 1
        array = [1]
        res = select(array, 0, len(array) - 1, len(array) - k + 1, k)
        expected = [1]
        self.assertEquals(expected, res)

    def test_simple(self):
        k = 2
        array = [1, 2, 3, 4, 5]
        res = select(array, 0, len(array) - 1, len(array) - k + 1, k)
        expected = [4, 5] or [5, 4]
        self.assertEquals(expected, res)

    def test_hard(self):
        k = 2
        array = [1, 4000, 7000000, 9, 2, 5, 14, 228, 666, 2742, 1458, 5647, 5642, 5648, 5644]
        res = select(array, 0, len(array) - 1, len(array) - k + 1, k)
        expected = [5648, 7000000] or [7000000, 5648]
        self.assertEquals(expected, res)
