import unittest
import part_one


class TestSorting(unittest.TestCase):
    def test_one(self):
        my_heap = lab8.MinHeap()
        k = 0
        a = [-5, -3, -6, 8, 9, 5]
        lab8.test(k, a, my_heap)
        res = my_heap.print_array()
        expected = []
        self.assertEqual(expected, res)

    def test_two(self):
        my_heap = lab8.MinHeap()
        k = 1
        a = [-5, -3, -6, 8, 9, 5]
        lab8.test(k, a, my_heap)
        res = my_heap.print_array()
        expected = [9]
        self.assertEqual(expected, res)

    def test_three(self):
        my_heap = lab8.MinHeap()
        k = 6
        a = [-5, -3, -6, 8, 9, 5]
        lab8.test(k, a, my_heap)
        res = my_heap.print_array()
        expected = [-6, -3, -5, 8, 9, 5]
        self.assertEqual(expected, res)

    def test_four(self):
        my_heap = lab8.MinHeap()
        k = 2
        a = [2, 7, 4, 2]
        lab8.test(k, a, my_heap)
        res = my_heap.print_array()
        expected = [4, 7]
        self.assertEqual(expected, res)
