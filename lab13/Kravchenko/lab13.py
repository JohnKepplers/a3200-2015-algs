class Node:
    """ Class for single node """

    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class SplayTree:
    def __init__(self):
        self.root = None

    def set_parent(self, child, parent):
        """ First auxiliary function for working with pointer to parents """
        if child != None:
            child.parent = parent

    def keep_parent(self, v):
        """ Second auxiliary function for working with pointer to parents """
        self.set_parent(v.left, v)
        self.set_parent(v.right, v)

    def rotate(self, parent, child):
        """ If you call any vertex, it will go to the root """
        grandparent = parent.parent
        if grandparent != None:
            if grandparent.left == parent:
                grandparent.left = child
            else:
                grandparent.right = child

        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent
        self.keep_parent(child)
        self.keep_parent(parent)
        child.parent = grandparent

    def splay(self, v):
        """ When our vertex go to the root,
        distance to the root is reduced not only for raising the top, but for all her descendants in the current subtrees """
        if v.parent == None:
            return v
        parent = v.parent
        grandparent = parent.parent
        if grandparent == None:
            self.rotate(parent, v)
            return v
        else:
            zigzig = (grandparent.left == parent) == (parent.left == v)
            if zigzig:
                self.rotate(grandparent, parent)
                self.rotate(parent, v)
            else:
                self.rotate(parent, v)
                self.rotate(grandparent, v)
            return self.splay(v)

    def find(self, v, key):
        if v == None:
            return None
        if key == v.key:
            return self.splay(v)
        if key < v.key and v.left != None:
            return self.find(v.left, key)
        if key > v.key and v.right != None:
            return self.find(v.right, key)

        return self.splay(v)

    def split(self, root, key):
        if root == None:
            return None, None
        root = self.find(root, key)
        if root.key == key:
            self.set_parent(self.root.left, None)
            self.set_parent(self.root.right, None)
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
        if right == None:
            return left
        if left == None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    ''' '''

    def insert(self, root, key):
        left, right = self.split(root, key)
        root = Node(key, left, right)
        self.keep_parent(root)
        return root

    def remove(self, root, key):
        root = self.find(root, key)
        self.set_parent(root.left, None)
        self.set_parent(root.right, None)
        return self.merge(root.left, root.right)

    def iterate(self):
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
