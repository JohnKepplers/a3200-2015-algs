import t_sort
import unittest


class TestTopologicalSort(unittest.TestCase):
    def test_for_graph_without_cycles(self):
        graph = t_sort.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(5, 6)
        res = graph.topological_sort(graph.a)
        expected = [42, 1, 2, 4, 5, 6, 3] or [1, 2, 4, 5, 6, 3, 42] or [1, 2, 3, 4, 5, 6, 42] or [42, 1, 2, 3, 4, 5, 6]
        self.assertEquals(expected, res)

    def test_for_graph_with_cycles(self):
        graph = t_sort.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(5, 6)
        graph.add_directed_link(6, 6)
        res = graph.topological_sort(graph.a)
        expected = None
        self.assertEquals(expected, res)
