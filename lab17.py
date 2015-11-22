class WeightedGraph:
    def __init__(self):
        self.a = [[]]
        self.tree = [[]]
        self.d = {}
        self.list = []

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
        for k in range(1, self.size_of_matrix()):
            self.a[k] += [0]
        self.a += [[0] * self.size_of_matrix()]

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
        for j in range(len(self.a[0])):
            self.tree[0] += [self.a[0][j]]
            for k in range(1, self.size_of_tree()):
                self.tree[k] += [0]
            self.tree += [[0] * self.size_of_tree()]
        self.list.sort()
        print(self.list)
        print(self.d)
        for f in range(len(self.list)):
            array = self.d[self.list[f]]
            print(array)
            for j in range(0, len(array), 2):
                index_one = self.a[0].index(array[j]) + 1
                index_two = self.a[0].index(array[j + 1])
                index_three = self.a[0].index(array[j+1]) + 1
                index_four = self.a[0].index(array[j])
                print(self.a[index_one][index_two])
                if self.tree[index_one][index_two] == 0:
                    self.tree[index_one][index_two] = self.a[index_one][index_two]
                    self.tree[index_three][index_four] = self.a[index_three][index_four]
                    print(self.tree)



if __name__ == '__main__':
    graph = WeightedGraph()
    for i in range(1, 5):
        graph.add_vertex(i)
    graph.add_directed_link(1, 2, 4)
    graph.add_directed_link(2, 3, 4)
    graph.add_directed_link(1, 3, 2)
    graph.add_directed_link(3, 4, 3)
    graph.min_tree()
    print(graph.print_matrix())
    print(graph.print_tree())
