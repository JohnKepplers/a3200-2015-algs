from sys import maxsize as vasiliy_pisar
import heapq


class WeightedGraph:
    def __init__(self):
        self.a = [[42], [0]]
        self.list = []
        self.d = {42: [vasiliy_pisar, None]}

    def size_of_matrix(self):
        return len(self.a)

    def print_matrix(self):
        return self.a

    def size_of_list(self):
        return len(self.list)

    def add_vertex(self, v):
        if self.size_of_matrix() == 2:
            self.a[0] = [v]
            self.d = {v: [vasiliy_pisar, None]}
        self.a[0] += [v]
        self.d.update({v: [vasiliy_pisar, None]})
        for i in range(1, self.size_of_matrix()):
            self.a[i] += [0]
        self.a += [[0] * self.size_of_matrix()]

    def add_directed_link(self, v1, v2, weight):
        if self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] == 0:
            self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] = weight
            self.d.update({v2: [weight, v1]})

        else:
            print('Error: these vertex already have rib.')

    def relax(self, u, v, weight):
        if self.d[v][0] > self.d[u][0] + weight:
            self.d[v][0] = self.d[u][0] + weight
            self.d[v][1] = u

    def initialize_single_source(self, s):
        for key, value in self.d.items():
            self.d[key][0] = vasiliy_pisar
            self.d[key][1] = None
        self.d[s][0] = 0

    def dijkstra(self, s):
        self.initialize_single_source(s)
        q = []
        for key in self.d.keys():
            q += [key]
        while len(q) != 0:
            u = heapq.heappop(q)
            self.list.append(u)
            for key in self.d.keys():
                if self.a[self.a[0].index(u) + 1][self.a[0].index(key)] != 0:
                    self.relax(u, key, self.a[self.a[0].index(u) + 1][self.a[0].index(key)])
        array = []
        for key in self.d.keys():
            array += [self.d[key][0]]
        return array
