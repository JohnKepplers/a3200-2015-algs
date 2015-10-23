from random import randint, random

__author__ = 'alexkane'

import unittest
import lab9
import lab9part2

class TestSorting(unittest.TestCase):

    def part1_test_trivial(self):
        queue = lab9.HeapPriorityQueue()
        queue.set_special_k(1)
        queue.insert(2)
        queue.insert(1)
        expected = 2
        res = queue.get_array()[0]
        self.assertEqual(expected, res)

    def part1_test_hardcore(self):
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

    def part2_test_trivial(self):
        array = [1, 0, 8, 2, 1]
        res = lab9part2.quick_search(array, 0, 5)
        expected = [0, 1, 1, 2, 8]
        self.assertEqual(expected, res)