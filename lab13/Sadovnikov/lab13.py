__author__ = 'alexkane'


class Node:
    """Simple class that represents nodes in tree."""

    def __init__(self, key, left, right, parent):
        """Four fields need to be initialized.

        key -- represents value stored in node
        left -- link to left child of a node
        right -- link to the right child of a node
        parent -- link to the parent of a node
        """

        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class SplayTree():
    """Splay Tree itself.

    Splay tree is self-adjusting binary search tree. Pros of using this type of trees are that tree doesn't need to keep
    any extra information about itself, what makes it efficient in terms of memory usage, also splay tree works much
    faster than other types of binary trees when working with real input data.
    In situations, when we work with already built binary search tree and need to respond to queries such as "whether
    this key is present in the tree or not", and the user is mostly interested in one key and queries others only from
    time to time, we might face a problem of processing m number of queries in O(m log(n)) time. But splay tree will
    process such number of queries in O(m) due to its self-adjusting structure.
    Obvious disadvantage of splay tree is that its height can be linear, Although all its methods still work in
    amortized O(log(n)) time.

    Algorithm:
    Accessing any of the nodes executes splay operation that moves accessed node to the root ot the tree. Splaying
    consists of two steps: zig ,zig-zig and zig-zag. Let's assume that current node is x, parent is parent of x and
    grandparent is parent of parent. Zig step is done when parent of x is the root. The tree is rotated from x to p.
    Zig-zig is done when parent is not the root and x and parent are either both right children or are both left
    children. The tree is rotated from parent to grandparent, then rotated from x to parent. Zig-zag is done when parent
    is not the root and x is a right child and parent is a left child. The tree is rotated from x to parent, and then
    rotated from x to grandparent.
    """

    def __init__(self):
        """Only one field needs to be initialized by default.

        root -- root of this tree
        """

        self.root = None

    def __iter__(self):
        """Method responsible for iteration."""
        return self.iterate()

    def set_parent(self, child, parent):
        """Helper method to link chosen node with another chosen node.

        child -- node which parent is set
        parent -- node being linked as parent to another node
        """

        if child is not None:
            child.parent = parent

    def keep_parent(self, v):
        """Helper method to set links between this node and its children.

        v -- chosen node
        """

        self.set_parent(v.left, v)
        self.set_parent(v.right, v)

    def rotate(self, parent, child):
        """Method that performs standard rotation of nods in chosen direction.

        parent -- node in which direction rotation is being done
        child -- node from which rotation is being done
        """

        gparent = parent.parent
        if gparent is not None:
            if gparent.left == parent:
                gparent.left = child
            else:
                gparent.right = child

        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent

        self.keep_parent(child)
        self.keep_parent(parent)
        child.parent = gparent

    def splay(self, v):
        """Main method in whole tree which performs transferring of a chosen node to the root of the tree keeping its features.

        v -- node that is being transferred
        """

        if v.parent is None:
            self.root = v
            return v
        parent = v.parent
        gparent = parent.parent
        if gparent is None:
            self.rotate(parent, v)
            self.root = v
            return v
        else:
            zigzig = (gparent.left == parent) == (parent.left == v)
            if zigzig:
                self.rotate(gparent, parent)
                self.rotate(parent, v)
            else:
                self.rotate(parent, v)
                self.rotate(gparent, v)
            self.root = self.splay(v)
            return self.root

    def split(self, root, key):
        """Helper method that performs splitting of a tree into two different ones, in one of which are stored nodes with
        value less than the key and in the other nodes with value greater than the key.

        root -- root of the tree
        key -- key by which we divide the tree
        """

        if root is None:
            return None, None
        root = self.find(root, key)
        if root == key:
            self.set_parent(root.left, None)
            self.set_parent(root.right, None)
            return root.left, root.right
        if root.key < key:
            right, root.right = root.right, None
            self.set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            self.set_parent(left, None)
            return left, root

    def merge(self, left, right):
        """Helper method that merges two trees into one.

        left -- left tree
        right -- right tree
        """

        if right is None:
            return left
        if left is None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    def find(self, v, key):
        """Method that searches the tree for node with set key and moves it to the root of the tree.

        v -- current node
        key -- value that needs to be found
        """

        if v is None:
            return None
        if key == v.key:
            return self.splay(v)
        if key < v.key and v.left is not None:
            return self.find(v.left, key)
        if key > v.key and v.right is not None:
            return self.find(v.right, key)
        return self.splay(v)

    def add(self, key):
        """Method that adds value to the tree.

        key -- value to add
        """

        left, right = self.split(self.root, key)
        self.root = Node(key, left, right, None)
        self.keep_parent(self.root)
        return self.root

    def remove(self, key):
        """Method that removes set value from the tree.

        key -- value to remove
        """

        root = self.find(self.root, key)
        self.set_parent(root.left, None)
        self.set_parent(root.right, None)
        return self.merge(root.left, root.right)

    def contains(self, key):
        """Method that checks whether tree contains given value.

        key -- value
        """

        return self.find(self.root, key) == key

    def iterate(self):
        """Method used by __iter__ method to iterate the tree."""
        v = self.root
        while True:
            while v.left is not None:
                v = v.left
            k = self.splay(v)
            if k.right is not None:
                v = k.right
                yield k
            else:
                yield k
                break
