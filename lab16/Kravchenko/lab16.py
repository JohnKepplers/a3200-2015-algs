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
        print(self.d)
        for key, value in self.d.items():
            if self.d[key][1] is None:
                if self.d[key][0] < maxsize:
                    array += [[key]]
                else:
                    array += [[None]]
            else:
                ar = []
                this_key = key
                while self.d[this_key][1] is not None:
                    ar += [this_key]
                    this_key = self.d[this_key][1]
                ar += [this_key]
                ar.reverse()
                array += [ar]
        return array


if __name__ == '__main__':
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_directed_link(1, 4, 8)
    graph.add_directed_link(1, 2, 1)
    graph.add_directed_link(2, 3, 2)
    graph.add_directed_link(3, 4, 3)
    graph.add_directed_link(2, 4, 1)
    print(graph.paths(1))

