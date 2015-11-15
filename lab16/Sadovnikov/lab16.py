__author__ = 'vmath'

import heapq


class Node():
    def __init__(self, name):
        self.name = name
        self.outcoming_vertexes = {}
        self.path = float('inf')
        self.link = None

    def __lt__(self, other):
        return self.path < other.path


class WeightedGraph():
    def __init__(self):
        self.graph = []

    def add_vertex(self, v):
        self.graph.append(Node(v))

    def add_directed_link(self, v1, v2, weight):
        self.graph[v1].outcoming_vertexes[v2] = weight

    def relax(self, u, v, weight):
        if self.graph[v].path > self.graph[u].path + weight:
            self.graph[v].path = self.graph[u].path + weight
            self.graph[v].link = u

    def paths(self, w):
        q = []
        for vertex in self.graph:
            if vertex.name == w:
                vertex.path = 0
                vertex.link = w
            else:
                vertex.path = float('inf')
                vertex.link = None
            heapq.heappush(q, vertex)
        s = []
        while len(q) != 0:
            u = heapq.heappop(q)
            s.append(u)
            for key in u.outcoming_vertexes:
                self.relax(u.name, key, u.outcoming_vertexes[key])
        return [i.path for i in self.graph]

