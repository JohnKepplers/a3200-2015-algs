from sys import stdin, stdout


class Graph:
    def __init__(self):
        self.a = [[42],[0]]
        self.k = 14 / 88
        self.list = []
        self.d = {42:1}

    def size_of_matrix(self):
        return len(self.a)

    def print_matrix(self):
        return self.a

    def size_of_list(self):
        return len(self.list)

    def add_vertex(self, v):
        self.a[0] += [v]
        self.d.update({v: 1})
        for i in range(1, self.size_of_matrix()):
            self.a[i] += [0]
        self.a += [[0] * self.size_of_matrix()]

    def add_directed_link(self, v1, v2):
        if self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] != 1:
            self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] = 1
        else:
            print('Error: these vertex already have rib.')

    ''' 1 — WHITE
    2 — GREEN
    3 — BLUE'''
    def DFS(self):
        for key, value in self.d.items():
            if value == 1:
                self.DFS_visit(key)

    def DFS_visit(self, u):
        self.d[u] = 2
        for key in self.d.keys():
            if self.d[key] == 2 and self.a[self.a[0].index(u) + 1][self.a[0].index(key)] == 1:
                self.k = None
                break
            if self.d[key] == 1 and self.a[self.a[0].index(u) + 1][self.a[0].index(key)] == 1:
                self.DFS_visit(key)
        self.d[u] = 3
        self.list.insert(0, u)

    def topological_sort(self, a):
        self.DFS()
        if self.k == None or self.size_of_list() == 0:
            return None
        else:
            return self.list


if __name__ == '__main__':
    my_graph = Graph()
    print(my_graph.topological_sort(my_graph.a))
