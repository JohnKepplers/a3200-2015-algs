from random import randint, random

__author__ = 'alexkane'

class DSU():
    def __init__(self, n):
        self.parent = n * [None]

    def MakeSet(self, x):
        self.parent[x] = x

    def Find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Unite(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if randint(1, 2) == 1:
            x, y = y, x
        self.parent[x] = y
