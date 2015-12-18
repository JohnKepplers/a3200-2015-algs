from ilya import rectangular
import unittest


class Test(unittest.TestCase):
    def test_trivial(self):
        res = rectangular(4, [2, 4, 4, 3])
        expected = 8
        self.assertEqual(expected, res)

    def test_big(self):
        res = rectangular(23, [9, 5, 6, 7, 8, 3, 4, 3, 4, 3, 2, 3, 32, 23, 24, 1, 1, 1, 1, 3, 4, 4, 4])
        expected = 235
        self.assertEquals(expected, res)
