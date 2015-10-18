from random import randint
import unittest
import lab6 # import radix_sort.py from current directory

class TestSorting(unittest.TestCase):

    def test_trivial(self):
        arr = [1, 333, 22]
        res = lab6.radix_sort(arr)
        expected = [1, 22, 333]

        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = lab6.radix_sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_consecutive_integers(self):
        arr = [i for i in range(100000)]
        res = lab6.radix_sort(arr)
        subject = 0
        for x in range (100000):
            if res[x] >= subject:
                subject = res[x]
            else:
                subject = -1
                break
        self.assertTrue(subject != -1)

    def test_not_trivial(self):
        arr = [randint(0, 100000) for i in range(100000)]
        res = lab6.radix_sort(arr)
        subject = 0
        for x in range (100000):
            if res[x] >= subject:
                subject = res[x]
            else:
                subject = -1
                break
        self.assertTrue(subject != -1)

    def test_same_element(self):
        arr = [1000000 for i in range(100000)]
        res = lab6.radix_sort(arr)
        subject = 0
        for x in range (100000):
            if res[x] >= subject:
                subject = res[x]
            else:
                subject = -1
                break
        self.assertTrue(subject != -1)

    def test_negative_element(self):
        arr = [-1, -333, -22]
        res = lab6.radix_sort(arr)
        expected = [-333, -22, -1]

        self.assertEqual(expected, res)