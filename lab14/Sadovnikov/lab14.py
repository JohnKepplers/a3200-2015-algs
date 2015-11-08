# coding=utf-8
__author__ = 'alexkane'

from sys import stdin


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph[v] = ['white']

    def add_directed_link(self, v1, v2):
        self.graph[v1].append(v2)

    def topological_sort(self):
        list = DFS(self.graph)
        return list[::-1]


def DFS(graph):
    list = []
    for key in graph:
        if graph[key][0] == 'white':
            DFS_Visit(graph, graph[key], key, list)
    return list


def DFS_Visit(graph, vertex, key, list):
    vertex[0] = 'green'
    for i in range(1, len(vertex)):
        if graph[vertex[i]][0] == 'white':
            DFS_Visit(graph, graph[vertex[i]], vertex[i], list)
    vertex[0] = 'blue'
    list.append(key)

