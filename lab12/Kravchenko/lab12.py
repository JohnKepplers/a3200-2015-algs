class Set:
    def add(self, key):
        pass

    def iterate(self):
        pass


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class UnbalancedBinarySearchTree(Set):
    def __init__(self):
        self.root = None
        self.max = None
        self.how_many_nodes_on_the_my_binary_christmas_tree = 0
        self.deep = 0
        self.helping_node = None
        self.number = 0
        self.a = None

    def __iter__(self):
        return self.iterate()

    def search(self, x, k):
        if x is None:
            return False
        if k == x.key:
            return True
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def add(self, key):
        x = self.root
        z = Node(key)
        if x is None:
            self.root = Node(key)
            self.max = key
            self.how_many_nodes_on_the_my_binary_christmas_tree += 1
            return
        while x is not None:
            if key > x.key:
                if x.right is not None:
                    x = x.right
                else:
                    z.parent = x
                    x.right = z
                    self.how_many_nodes_on_the_my_binary_christmas_tree += 1
                    if key > self.max:
                        self.max = key
                    break
            elif key < x.key:
                if x.left is not None:
                    x = x.left
                else:
                    self.how_many_nodes_on_the_my_binary_christmas_tree += 1
                    z.parent = x
                    x.left = z
                    parent_node = x
                    break

    def next_node(self, node):
        while node.key < self.max:
            if node.right is not None and self.a is not None and node.key == self.a.key:

                self.a = node.right
                self.helping_node = None
                self.deep = 0
                this_node = node.right
                while this_node.left is not None:
                    this_node = this_node.left
                return this_node
            if node.right is None and node.left is None and self.helping_node is not None and self.helping_node is not None and node is node.parent.right:
                print(node.key, self.deep)
                while self.deep > 0:
                    self.deep -= 1
                    node = node.parent
                self.helping_node = None
                return node.parent
            if node.right is None:
                return node.parent

            this_node = node.right
            self.helping_node = node.right
            while this_node.left is not None:
                this_node = this_node.left
            self.deep += 1

            return this_node
        return node

    def iterate(self):
        self.a = self.root
        if self.root is not None:
            this_node = self.root
            while this_node.left is not None:
                this_node = this_node.left
            current_node = this_node
            self.number += 1
            for i in range(self.how_many_nodes_on_the_my_binary_christmas_tree):
                yield current_node.key
                current = self.next_node(current_node)
