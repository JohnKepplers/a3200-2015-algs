from sys import stdin

__author__ = 'alexkane'

class Node():
    def __init__(self, name):
        self.name = name
        self.links = []
        self.colour = "white"
        self.height = 0

    def __lt__(self, other):
        return self.height < other.height

class Graph:
    def __init__(self, n, king_vertex, links):
        self.graph = []
        self.heap = []
        self.tree = {}
        self.n = n
        self.king_vertex = king_vertex
        for x in range(n):
            self.graph.append(Node(x))
        self.add_links(links)
        self.enter_array = []

    def add_links(self, array):
        for x in array:
            self.graph[x[0]].links.append(x[1])
            self.graph[x[1]].links.append(x[0])

    def dfs(self):
        self.enter_array = []
        for x in self.graph:
            x.colour = "white"
        height = 0
        self.dfs_visit(self.graph[self.king_vertex], height)

    def dfs_visit(self, vertex, height):
        bool = True
        height += 1
        vertex.colour = "green"
        vertex.height = height
        for x in vertex.links:
            if self.graph[x].colour == "white":
                self.dfs_visit(self.graph[x], height)
                if bool:
                    self.enter_array.append(vertex.name)
                    bool = False
        if bool:
            self.enter_array.append(vertex.name)
        vertex.colour = "blue"

    def build_wicked_tree(self, tree, array, n):
        for i in range(0, n):
            tree[n - 1 + i] = self.graph[array[i]]
        for i in range(n - 2, -1, -1):
            tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

    def search_wicked_tree(self, left, right):
        leftRes = Node('theLeft')
        leftRes.height = float('inf')
        rightRes = Node('theRight')
        rightRes.height = float('inf')
        while left < right:
            if left % 2 == 0:
               leftRes = min(leftRes, self.tree[left])
            left = left // 2
            if right % 2 == 1:
               rightRes = min(rightRes, self.tree[right])
            right = (right - 2) // 2
        if left == right:
            leftRes = min(leftRes, self.tree[left])
        return min(leftRes, rightRes)

    def pre_process(self):
        self.dfs()
        self.tree = {}
        self.enter_array = self.enter_array
        self.build_wicked_tree(self.tree, self.enter_array, len(self.enter_array))

    def execute(self, v1, v2):
        r = len(self.enter_array) - self.enter_array[::-1].index(v2) - 1
        l = self.enter_array.index(v1)
        left = min(l, r)
        right = max(l, r)
        return self.search_wicked_tree(left + len(self.tree) // 2, right + len(self.tree) // 2).name


if "__name__" == "__main__":
    n = stdin.readline()
    king = stdin.readline()
    array = []
    for i in range(0, n - 1):
        line = [x for x in stdin.readline().split(' ')]
        array.append((line[0], line[1]))
    graph = Graph(n, king, array)
    graph.pre_process()
    for line in stdin.readlines():
        line = [x for x in stdin.readline().split(' ')]
        print(graph.execute(line[0], line[1])),
