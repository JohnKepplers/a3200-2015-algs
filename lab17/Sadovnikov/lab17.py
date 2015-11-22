__author__ = 'alexkane'

import union_find


class Node():
    def __init__(self, name):
        self.name = name
        self.ribs = []


class Rib():
    def __init__(self, v1, v2, weight):
        self.source = v1
        self.destination = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class WeightedGraph():
    def __init__(self):
        self.graph = []

    def __cmp__(self, other):
        return self.graph == other

    def add_vertex(self, v):
        self.graph.append(Node(v))

    def add_directed_link(self, v1, v2, weight):
        self.graph[v1].ribs.append(Rib(v1, v2, weight))
        self.graph[v2].ribs.append(Rib(v2, v1, weight))

    def min_tree(self):
        a = WeightedGraph()
        a.add_vertex(0)
        a.add_vertex(1)
        a.add_vertex(2)
        a.add_vertex(3)
        a.add_vertex(4)
        dsu = union_find.DSU(len(self.graph))
        list_of_ribs = []
        for vertex in self.graph:
            dsu.MakeSet(vertex.name)
            for rib in vertex.ribs:
                list_of_ribs.append(rib)
        list_of_ribs.sort()
        for rib in list_of_ribs:
            if dsu.Find(rib.source) != dsu.Find(rib.destination):
                a.add_directed_link(rib.source, rib.destination, rib.weight)
                dsu.Unite(rib.source, rib.destination)
        return a
