from union_find import DisjointSetUnion


class WeightedGraph:
    def __init__(self):
        self.a = [[]]
        self.tree = [[]]
        self.d = {}
        self.list = []
        self.maximum = None

    def size_of_matrix(self):
        return len(self.a)

    def print_matrix(self):
        return self.a

    def size_of_tree(self):
        return len(self.tree)

    def print_tree(self):
        return self.tree

    def add_vertex(self, v):
        self.a[0] += [v]
        for i in range(1, self.size_of_matrix()):
            self.a[i] += [0]
        self.a += [[0] * self.size_of_matrix()]
        if self.maximum is None:
            self.maximum = v
        else:
            if self.maximum < v:
                self.maximum = v

    def add_directed_link(self, v1, v2, weight):
        if self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] == 0:
            self.a[self.a[0].index(v1) + 1][self.a[0].index(v2)] = weight
            self.a[self.a[0].index(v2) + 1][self.a[0].index(v1)] = weight
            if self.d.get(weight) is None:
                self.d.update({weight: [v1, v2]})
                self.list.append(weight)
            else:
                self.d[weight] += [v1, v2]

        else:
            print('Error: these vertex already have rib.')

    def get_links(self, v):
        array = []
        index = self.a[0].index(v)
        for i in range(1, self.size_of_matrix()):
            if self.a[i][index] != 0:
                array.append(self.a[0][self.a.index(self.a[i]) - 1])
        return array

    def min_tree(self):
        n = self.maximum
        n += 1
        my_disjoint_set_union = DisjointSetUnion(len(self.a[0]))
        for j in range(len(self.a[0])):
            my_disjoint_set_union.make_set(self.a[0][j])
            self.tree[0] += [self.a[0][j]]
            for k in range(1, self.size_of_tree()):
                self.tree[k] += [0]
            self.tree += [[0] * self.size_of_tree()]
        self.list.sort()
        for i in range(len(self.list)):
            array = self.d[self.list[i]]
            for j in range(0, len(array), 2):
                if my_disjoint_set_union.find(array[j]) != my_disjoint_set_union.find(array[j + 1]):
                    index_one = self.a[0].index(array[j])
                    index_two = self.a[0].index(array[j + 1])
                    my_disjoint_set_union.unite(array[j], array[j + 1])
                    self.tree[index_one + 1][index_two] = self.a[index_one + 1][index_two]
                    self.tree[index_two + 1][index_one] = self.a[index_two + 1][index_one]


if __name__ == '__main__':
    graph = WeightedGraph()
    for k in range(4):
        graph.add_vertex(k)
    graph.add_directed_link(0, 1, 4)
    graph.add_directed_link(1, 2, 3)
    graph.add_directed_link(2, 3, 1)
    graph.add_directed_link(0, 3, 2)
    graph.min_tree()
    print(graph.print_matrix())
    print(graph.print_tree())
