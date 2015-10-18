from random import randint

__author__ = 'alexkane'

import unittest
import lab9

class TestSorting(unittest.TestCase):

    def test_trivial(self):
        queue = lab9.HeapPriorityQueue()
        queue.set_special_k(1)
        queue.insert(2)
        queue.insert(1)
        expected = 2
        res = queue.get_array()[0]
        self.assertEqual(expected, res)

    def test_hardcore(self):
        queue = lab9.HeapPriorityQueue()
        queue.set_special_k(10)
        for i in range(101):
            if i % 10 != 0:
                queue.insert(randint(-1000, 1000))
            else:
                queue.insert(1111)
        expected = [1111, 1111, 1111, 1111, 1111, 1111, 1111, 1111, 1111, 1111]
        res = queue.get_array()
        self.assertEqual(expected, res)