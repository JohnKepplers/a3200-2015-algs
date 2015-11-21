import lab16
import unittest
from sys import maxsize as vasiliy_pisar


class Test(unittest.TestCase):
    def test_veteran(self):
        graph = lab_14.WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(9)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_directed_link(1, 5, 3)
        graph.add_directed_link(5, 9, 7)
        graph.add_directed_link(1, 9, 11)
        graph.add_directed_link(9, 1, 1941)
        res = graph.dijkstra(1)
        expected = [0, vasiliy_pisar, 3, 10]
        self.assertEquals(expected, res)

    def test_big(self):
        graph = lab_14.WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_directed_link(1, 2, 1)
        graph.add_directed_link(2, 1, 1)
        graph.add_directed_link(2, 6, 8)
        graph.add_directed_link(6, 3, 4)
        graph.add_directed_link(3, 5, 9)
        graph.add_directed_link(5, 6, 1)
        graph.add_directed_link(6, 1, 5)
        graph.add_directed_link(5, 2, 11)
        graph.add_directed_link(4, 5, 6)
        graph.add_directed_link(4, 1, 13)
        graph.add_directed_link(3, 1, 8)
        graph.add_directed_link(1, 3, 9)
        res = graph.dijkstra(1)
        expected = [0, 1, 9, 2147483647, 18, 9]
        self.assertEquals(expected, res)
