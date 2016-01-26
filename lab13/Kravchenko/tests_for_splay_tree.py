import unittest
import splay_tree


class Test(unittest.TestCase):
    def test_empty(self):
        array = []
        tree = splay_tree.SplayTree()
        for v in tree:
            array.append(v.key)
        expected = []
        self.assertEquals(expected, array)

    def test_simple(self):
        array = []
        tree = splay_tree.SplayTree()
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(5)
        tree.add(4)
        for v in tree:
            array.append(v.key)
        expected = [1, 2, 3, 4, 5]
        self.assertEquals(expected, array)

    def test_hard(self):
        array = []
        tree = splay_tree.SplayTree()
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(5)
        tree.add(4)
        tree.add(23)
        tree.add(1231)
        tree.add(124)
        tree.add(123)
        tree.add(42)
        tree.add(547)
        tree.add(353)
        tree.add(242)
        tree.add(23424)
        tree.add(0)
        tree.add(-4)
        for v in tree:
            array.append(v.key)
        expected = [-4, 0, 1, 2, 3, 4, 5, 23, 42, 123, 124, 242, 353, 547, 1231, 23424]
        self.assertEquals(expected, array)
