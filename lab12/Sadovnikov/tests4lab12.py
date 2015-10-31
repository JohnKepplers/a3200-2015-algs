__author__ = 'alexkane'

import unittest
import lab12

class TestBSC(unittest.TestCase):

    def trivial_test(self):
        set = lab12.UnbalancedBinarySearchTree()
        set.add(6)
        set.add(9)
        set.add(8)
        set.add(3)
        set.add(4)
        set.add(2)
        set.add(88)
        set.add(7)
        set.add(1)
        set.add(99)
        set.add(10)
        set.add(21)
        set.add(5)
        set.add(77)
        set.add(88888)
        set.add(11)
        list = []
        for v in set:
            list.append(v.value)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 77, 88, 99, 88888]
        self.assertEquals(expected, list)

    def not_so_trivial_test(self):
        set = lab12.UnbalancedBinarySearchTree()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.add(6)
        set.add(100)
        set.add(21)
        set.add(19)
        set.add(18)
        set.add(17)
        set.add(9)
        set.add(10)
        set.add(11)
        set.add(12)
        set.add(13)
        list = []
        for v in set:
            list.append(v.value)
        expected = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 17, 18, 19, 21, 100]
        self.assertEquals(expected, list)