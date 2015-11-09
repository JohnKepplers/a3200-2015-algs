__author__ = 'alexkane'


class Graph:
    def __init__(self):
        self.graph = {}
        self.bool = True

    def add_vertex(self, v):
        self.graph[v] = ['white']

    def add_directed_link(self, v1, v2):
        self.graph[v1].append(v2)

    def topological_sort(self):
        return self.special_DFS(self.graph)

    def special_DFS(self, graph):
        list = []
        self.bool = True
        for key in graph:
            if graph[key][0] == 'white':
                self.special_DFS_Visit(graph, graph[key], key, list)
        if not self.bool:
            return None
        else:
            return list[::-1]

    def special_DFS_Visit(self, graph, vertex, key, list):
        vertex[0] = 'green'
        for i in range(1, len(vertex)):
            if self.bool:
                if graph[vertex[i]][0] == 'white':
                    self.special_DFS_Visit(graph, graph[vertex[i]], vertex[i], list)
                elif graph[vertex[i]][0] == 'blue':
                    new_bool = False
                    for x in graph[vertex[i]]:
                        if x != 'blue' and graph[x][0] == 'blue':
                            new_bool = True
                            break
                    if new_bool:
                        self.bool = False
                        break
            else:
                break
        vertex[0] = 'blue'
        list.append(key)
