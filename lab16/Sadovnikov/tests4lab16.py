__author__ = 'vmath'

import lab16
import unittest


class TestDijkstra(unittest.TestCase):
    def test_trivial(self):
        ex = lab16.WeightedGraph()
        ex.add_vertex(0)
        ex.add_vertex(1)
        ex.add_vertex(2)
        ex.add_vertex(3)
        ex.add_directed_link(0, 1, 1)
        ex.add_directed_link(0, 2, 3)
        ex.add_directed_link(2, 1, 5)
        ex.add_directed_link(1, 2, 1)
        res = ex.paths(0)
        expected = [0, 1, 2, float('inf')]
        self.assertEquals(expected, res)

    def test_trivial_1(self):
        ex = lab16.WeightedGraph()
        ex.add_vertex(0)
        ex.add_vertex(1)
        ex.add_vertex(2)
        ex.add_vertex(3)
        ex.add_directed_link(0, 1, 1)
        ex.add_directed_link(0, 2, 3)
        ex.add_directed_link(2, 1, 5)
        ex.add_directed_link(1, 2, 1)
        res = ex.paths(1)
        expected = [float('inf'), 0, 1, float('inf')]
        self.assertEquals(expected, res)

    def test_hardcore(self):
        ex = lab16.WeightedGraph()
        ex.add_vertex(0)
        ex.add_vertex(1)
        ex.add_vertex(2)
        ex.add_vertex(3)
        ex.add_vertex(4)
        ex.add_directed_link(0, 1, 10)
        ex.add_directed_link(0, 2, 5)
        ex.add_directed_link(1, 3, 1)
        ex.add_directed_link(1, 2, 2)
        ex.add_directed_link(2, 1, 3)
        ex.add_directed_link(2, 3, 9)
        ex.add_directed_link(2, 4, 2)
        ex.add_directed_link(3, 4, 4)
        ex.add_directed_link(4, 3, 6)
        ex.add_directed_link(4, 0, 7)
        res = ex.paths(0)
        expected = [0, 8, 5, 9, 7]
        self.assertEquals(expected, res)

    def test_unreal_case(self):
        ex = lab16.WeightedGraph()
        ex.add_vertex(0)
        ex.add_vertex(1)
        ex.add_vertex(2)
        ex.add_vertex(3)
        ex.add_vertex(4)
        ex.add_directed_link(1, 3, 1)
        ex.add_directed_link(1, 2, 2)
        ex.add_directed_link(2, 1, 3)
        ex.add_directed_link(2, 3, 9)
        ex.add_directed_link(2, 4, 2)
        ex.add_directed_link(3, 4, 4)
        ex.add_directed_link(4, 3, 6)
        ex.add_directed_link(4, 0, 7)
        res = ex.paths(0)
        expected = [0, float('inf'), float('inf'), float('inf'), float('inf')]
        self.assertEquals(expected, res)
