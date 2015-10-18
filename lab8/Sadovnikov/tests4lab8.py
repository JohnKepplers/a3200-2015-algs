from random import randint
import unittest
import lab8

class TestSorting(unittest.TestCase):

    def test_trivial(self):
        queue = lab8.MaxElementQueue()
        queue.push(8)
        queue.push(1)
        queue.push(3)
        queue.push(4)
        queue.push(2)
        queue.push(0)
        queue.push(0)
        queue.push(0)
        res = queue.max()
        expected = 8
        self.assertEqual(expected, res)

    def test_trivial_2(self):
        queue = lab8.MaxElementQueue()
        queue.push(8)
        queue.push(1)
        queue.push(3)
        queue.push(4)
        queue.push(2)
        queue.push(0)
        queue.push(0)
        queue.push(0)
        queue.pop()
        queue.pop()
        queue.pop()
        queue.pop()
        queue.pop()
        queue.pop()
        res = queue.max()
        expected = 0
        self.assertEqual(expected, res)


    def test_trivial_3(self):
        queue = lab8.MaxElementQueue()
        queue.push(8)
        queue.push(1)
        queue.push(3)
        queue.push(4)
        queue.push(2)
        queue.push(0)
        queue.push(0)
        queue.push(0)
        queue.pop()
        queue.pop()
        queue.pop()
        queue.push(3)
        res = queue.max()
        expected = 4
        self.assertEqual(expected, res)


    def test_erofeev(self):
        queue = lab8.MaxElementQueue()
        queue.push(3)
        queue.push(42)
        self.assertEqual(42, queue.max())
        self.assertEqual(3, queue.pop())
        self.assertEqual(42, queue.max())
        self.assertEqual(42, queue.pop())