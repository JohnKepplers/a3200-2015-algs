from random import randint, random

__author__ = 'alexkane'

class DSU():
    def __init__(self, n):
        self.parent = n * [None]
        self.rank = n * [None]

    def MakeSet(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def Find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Unite(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] = self.rank[x] + 1
