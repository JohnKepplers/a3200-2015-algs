import lab16
import unittest


class Test(unittest.TestCase):
    def test_small(self):
        graph = lab16.WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(9)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_directed_link(1, 5, 3)
        graph.add_directed_link(5, 9, 7)
        graph.add_directed_link(1, 9, 11)
        graph.add_directed_link(9, 1, 1941)
        res = graph.paths(1)
        expected = [[1], [None], [1, 5], [1, 5, 9]]
        self.assertEquals(expected, res)

    def test_big(self):
        graph = lab16.WeightedGraph()
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
        res = graph.paths(1)
        expected = [[1], [1, 2], [1, 3], [None], [1, 3, 5], [1, 2, 6]]
        self.assertEquals(expected, res)
