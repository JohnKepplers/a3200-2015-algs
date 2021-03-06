import unittest
from pythagoras import pythagoras
from random import randint
from time import time


class TestNumbers(unittest.TestCase):
    def test_egyptian(self):
        arr = [3, 5, 4]
        res = pythagoras(arr)
        expected = 1
        self.assertEqual(expected, res)

    def test_hard_egyptian(self):
        arr = [5, 4, 3, 5, 3, 5, 3, 4, 5, 4, 3, 5]
        res = pythagoras(arr)
        expected = 1
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = pythagoras(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_standard(self):
        arr = [23, 247, 19, 96, 264, 265, 132, 265, 181]
        res = pythagoras(arr)
        expected = 2
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    '''def test_for_time(self):
        arr = [randint(1, 100) for i in range(50000)]
        time1 = time()
        res = pythagoras(arr)
        time2 = time()
        print(time2-time1)
        expected = pythagoras(arr)
        self.assertEqual(expected, res)'''


    def test_another_one(self):
        arr = [12, 5, 3, 4, 13, 13, 13, 12, 5, 4, 1]
        res = pythagoras(arr)
        expected = 2
        self.assertEqual(expected, res)
