__author__ = 'alexkane'

class Set:
    def add(self, value):
        pass

    def iterate(self):
        pass

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

class UnbalancedBinarySearchTree(Set):
    def __init__(self):
        self.root = None
        self.max = -float('inf')

    def add(self, value):
        if value > self.max:
            self.max = value
        z = Node(value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

    def contains(self, x, value):
        if x == None:
            return False
        elif x.value == value:
            return True
        if value < x.value:
            return self.contains(x.left, value)
        else:
            return self.contains(x.right, value)

    def __iter__(self):
        # return TreeIterator(self)
        return self.iterate()

    def iterate(self):
        v = self.root
        while v.right is not None:
            v = v.right
        end = v.value
        v = self.root
        k = -float('inf')
        while v.left is not None:
                v = v.left
        while True:
            while v.value <= k:
                v = v.parent
            if v.value == end:
                if v.left is None or k >= v.left.value:
                    yield v.value
                    break
            if v.value > k and v.left is None:
                k = v.value
                if v.right is None:
                    v = v.parent
                else:
                    v = v.right
                yield k
            elif v.value > k and v.left is not None:
                if v.left.value > k:
                    while v.left is not None:
                        v = v.left
                k = v.value
                if v.right is None:
                    v = v.parent
                else:
                    v = v.right
                yield k
            elif v.right is not None and v.right.value <= k:
                k = v.value
                v = v.parent
                yield k
