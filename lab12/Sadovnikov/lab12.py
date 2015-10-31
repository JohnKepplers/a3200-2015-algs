__author__ = 'alexkane'

class Set:
    def add(self, value):
        pass

    def iterate(self):
        pass


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
        return TreeIterator(self)


class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class TreeIterator:
    def __init__(self, tree):
        self.tree = tree
        self.current = tree.root
        self.tricky_value = self.tree.root.value
        self.bool = False
        if self.current.left != None:
            while self.current.left != None:
                self.current = self.current.left
            self.current = self.current.parent
        else:
            self.bool = True

    def next(self):
        if self.tricky_value < self.tree.max or self.tricky_value == self.tree.root.value:
            if self.bool:
                self.bool = False
                return self.current
            else:
                if (self.current.left is not None and self.current.left.value > self.tricky_value) or (self.tricky_value == self.tree.root.value and self.current.value != self.tree.root.value):
                    while self.current.left is not None and self.current.left.value != self.tricky_value:
                        self.current = self.current.left
                        self.tricky_value = self.current.value
                    return self.current
                if self.current.right is not None and self.current.right.value > self.tricky_value:
                    if self.current.right.left is None:
                        self.current = self.current.right
                        self.tricky_value = self.current.value
                        return self.current
                    else:
                        self.current = self.current.right
                        while self.current.left is not None:
                            self.current = self.current.left
                        self.tricky_value = self.current.value
                        return self.current
                if self.current.value <= self.tricky_value:
                    while self.current.value <= self.tricky_value:
                        self.current = self.current.parent
                    self.tricky_value = self.current.value
                    if self.current.value != self.tree.root.value:
                        self.tricky_value = self.current.value
                        return self.current
                    else:
                        self.current = self.current.right
                        return self.current.parent
                self.current = self.current.parent
                self.tricky_value = self.current.value
                return self.current
        else:
            raise StopIteration()