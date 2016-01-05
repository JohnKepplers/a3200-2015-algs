__author__ = 'alexkane'

import unittest
import lab15

class TestSuffocation(unittest.TestCase):
    def test_Vovana(self):
        n = 8
        root = 2
        adjacent = [(0, 6), (3, 6), (6, 2), (4, 2), (1, 4), (5, 1), (7, 1)]
        graph = lab15.Graph(n, root, adjacent)
        graph.pre_process()
        self.assertEqual(graph.execute(0, 7), 2)
        self.assertEqual(graph.execute(5, 1), 1)
        self.assertEqual(graph.execute(1, 5), 1)
        self.assertEqual(graph.execute(0, 3), 6)

    def test_Vovana_again(self):
        n = 20
        root = 7
        adjacent = [(7, 5), (7, 13), (7, 11), (11, 4), (11, 19), (4, 6), (4, 0), (4, 1), (4, 3), (13, 15), (13, 14),
        (15, 16), (16, 17), (16, 18), (5, 2), (2, 8), (8, 9), (8, 12), (8, 10)]
        graph = lab15.Graph(n, root, adjacent)
        graph.pre_process()
        self.assertEqual(graph.execute(5, 13), 7)
        self.assertEqual(graph.execute(6, 19), 11)
        self.assertEqual(graph.execute(6, 12), 7)
        self.assertEqual(graph.execute(15, 10), 7)
        self.assertEqual(graph.execute(18, 14), 13)
        self.assertEqual(graph.execute(14, 2), 7)
        self.assertEqual(graph.execute(3, 19), 11)
        self.assertEqual(graph.execute(18, 15), 15)
        self.assertEqual(graph.execute(10, 2), 2)