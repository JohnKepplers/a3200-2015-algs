class DisjointSetUnion:
    def __init__(self, n):
        self.p = [None] * n
        self.r = [None] * n

    def make_set(self, x):
        self.p[x] = x
        self.r[x] = 1

    def find(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.r[x] < self.r[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.r[x] == self.r[y]:
                self.r[x] += 1
