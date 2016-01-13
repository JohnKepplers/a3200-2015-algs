import unittest
from lab12 import UnbalancedBinarySearchTree
from random import randint


class Test(unittest.TestCase):
    def test_contains_true(self):
        bst = UnbalancedBinarySearchTree()
        bst.add(3)
        bst.add(5)
        bst.add(4)
        bst.add(1)
        bst.add(8)
        george_boole = bst.search(bst.root, 1)
        expected = True
        self.assertEquals(expected, george_boole)

    def test_contains_false(self):
        bst = UnbalancedBinarySearchTree()
        bst.add(3)
        bst.add(5)
        bst.add(4)
        bst.add(1)
        bst.add(8)
        george_boole = bst.search(bst.root, 9)
        expected = False
        self.assertEquals(expected, george_boole)

    def test_empty(self):
        bst = UnbalancedBinarySearchTree()
        array = []
        for node in bst:
            array.append(node)
        expected = []
        self.assertEquals(expected, array)

    def test_trivial(self):
        bst = UnbalancedBinarySearchTree()
        array = []
        bst.add(1)
        for node in bst:
            array.append(node)
        expected = [1]
        self.assertEquals(expected, array)

    def test_small(self):
        bst = UnbalancedBinarySearchTree()
        array = []
        bst.add(5)
        bst.add(4)
        bst.add(7)
        bst.add(6)
        bst.add(2)
        bst.add(3)
        for node in bst:
            array.append(node)
        expected = [2, 3, 4, 5, 6, 7]
        self.assertEquals(expected, array)

    def test_big(self):
        bst = UnbalancedBinarySearchTree()
        array = []
        bst.add(5)
        bst.add(8)
        bst.add(6)
        bst.add(3)
        bst.add(2)
        bst.add(12)
        bst.add(13)
        bst.add(1)
        bst.add(0)
        bst.add(4)
        bst.add(120)
        bst.add(12122)
        bst.add(1223236)
        bst.add(1232352352)
        bst.add(123523523232)
        for node in bst:
            array.append(node)
        expected = [0, 1, 2, 3, 4, 5, 6, 8, 12, 13, 120, 12122, 1223236, 1232352352, 123523523232]
        self.assertEquals(expected, array)

    def test_very_big(self):
        bst = UnbalancedBinarySearchTree()
        array = []
        helping_array = []
        for i in range(77777):
            d = randint(0, 1000)
            if not bst.search(bst.root, d):
                bst.add(d)
                helping_array.append(d)
        helping_array.sort()
        for node in bst:
            array.append(node)
        expected = helping_array
        self.assertEquals(expected, array)
