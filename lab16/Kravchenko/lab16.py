from sys import maxsize, stdin, stdout
import heapq


class WeightedGraph:
    def __init__(self):
        self.graph = [[]]
        self.list = []
        self.d = {}

    def size_of_matrix(self):
        return len(self.graph)

    def print_matrix(self):
        return self.graph

    def size_of_list(self):
        return len(self.list)

    def add_vertex(self, v):
        self.graph[0] += [v]
        self.d.update({v: [maxsize, None]})
        for i in range(1, self.size_of_matrix()):
            self.graph[i] += [0]
        self.graph += [[0] * self.size_of_matrix()]

    def add_directed_link(self, v1, v2, weight):
        if self.graph[self.graph[0].index(v1) + 1][self.graph[0].index(v2)] == 0:
            self.graph[self.graph[0].index(v1) + 1][self.graph[0].index(v2)] = weight
            self.d.update({v2: [weight, v1]})

        else:
            print('Error: these vertex already have rib.')

    def relax(self, u, v, weight):
        if self.d[v][0] > self.d[u][0] + weight:
            self.d[v][0] = self.d[u][0] + weight
            self.d[v][1] = u

    def initialize_single_source(self, s):
        for key, value in self.d.items():
            self.d[key][0] = maxsize
            self.d[key][1] = None
        self.d[s][0] = 0

    def paths(self, w):
        self.initialize_single_source(w)
        q = []
        for key in self.d.keys():
            q += [key]
        while len(q) != 0:
            u = heapq.heappop(q)
            self.list.append(u)
            for key in self.d.keys():
                if self.graph[self.graph[0].index(u) + 1][self.graph[0].index(key)] != 0:
                    self.relax(u, key, self.graph[self.graph[0].index(u) + 1][self.graph[0].index(key)])
        array = []
        for key in self.d.keys():
            array += [self.d[key][0]]
        return array
if __name__ == '__main__':
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(9)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_directed_link(1, 5, 3)
    graph.add_directed_link(5, 9, 7)
    graph.add_directed_link(1, 9, 11)
    graph.add_directed_link(9, 1, 1941)
    print(graph.paths(1))
