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
        self.current_min_node = None

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
            self.current_min_node = key
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
                    if key < self.current_min_node:
                        self.current_min_node = key
                    break

    def next_node(self, node):
        if node.key == self.max:
            return node.key
        if node.left is not None:
            if node.left.key > self.current_min_node:
                while node.left is not None:
                    node = node.left
            self.current_min_node = node.key
            if node.right is None:
                this_node = node.parent
                if this_node.key > self.current_min_node:
                    return this_node
                else:
                    while this_node.key <= self.current_min_node:
                        this_node = this_node.parent
                    return this_node
            else:
                this_node = node.right
                while this_node.left is not None:
                    this_node = this_node.left
                return this_node
        else:
            self.current_min_node = node.key
            if node.right is None:
                this_node = node.parent
                while this_node.key <= self.current_min_node:
                    this_node = this_node.parent
                return this_node
            else:
                this_node = node.right
                if this_node.left is None:
                    return this_node
                else:
                    while this_node.left is not None:
                        this_node = this_node.left
                return this_node

    def iterate(self):
        if self.current_min_node is not None:
            self.current_min_node -= 1
        if self.root is not None:
            this_node = self.root
            while this_node.left is not None:
                this_node = this_node.left
            current_node = this_node
            for i in range(self.how_many_nodes_on_the_my_binary_christmas_tree):
                yield current_node.key
                current_node = self.next_node(current_node)
