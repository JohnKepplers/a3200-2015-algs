import unittest
import stacks

class TestSorting(unittest.TestCase):
    def test_for_empty_queue(self):
        queue = stacks.StacksQueueWithMaxElement()
        queue.push(2)
        queue.push(2)
        queue.push(8)
        queue.pop()
        queue.pop()
        queue.pop()
        res = queue.max()
        expected = 'empty'
        self.assertEqual(expected, res)


    def test_lost(self):
        queue = stacks.StacksQueueWithMaxElement()
        queue.push(4)
        queue.push(8)
        queue.push(15)
        queue.push(16)
        queue.push(23)
        queue.push(42)
        queue.push(0)
        queue.push(0)
        queue.push(0)
        res = queue.max()
        expected = 42
        self.assertEqual(expected, res)

    def another_stupid_test(self):
        queue = stacks.StacksQueueWithMaxElement()
        queue.push(3)
        queue.push(6)
        queue.push(0)
        queue.push(7)
        queue.push(6)
        queue.push(3)
        queue.push(0)
        queue.push(1)
        queue.pop()
        queue.pop()
        queue.pop()
        queue.pop()
        queue.pop()
        res = queue.max()
        expected = 3
        self.assertEqual(expected, res)
