import lab17
import unittest


class Test(unittest.TestCase):
    def test_trivial(self):
        my_graph = lab17.WeightedGraph()
        my_graph.add_vertex(1)
        my_graph.add_vertex(2)
        my_graph.add_vertex(3)
        my_graph.add_directed_link(1, 2, 4)
        my_graph.add_directed_link(1, 3, 6)
        my_graph.add_directed_link(2, 3, 5)
        my_graph.min_tree()
        res = my_graph.print_tree()
        self.assertEqual([[1, 2, 3], [0, 4, 0], [4, 0, 5], [0, 5, 0]], res)
