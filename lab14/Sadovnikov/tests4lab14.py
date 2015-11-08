__author__ = 'alexkane'

import lab14
import unittest

class TestTopologicalSort(unittest.TestCase):

    def trivial_test(self):
        graph = lab14.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(4, 2)
        res = graph.topological_sort()
        expected = [1, 3, 4, 2]
        self.assertEquals(expected, res)