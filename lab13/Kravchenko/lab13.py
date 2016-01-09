class Node:
    """Class for single node"""

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
        if child is not None:
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
        """When our vertex go to the root,
        distance to the root is reduced not only for raising the top, but for all her descendants in the current subtrees
        """
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
        """After the vertex is found, we pull it up and do the root using the procedure splay"""
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
        """Split takes an key and the tree divides into two. In one tree all the values less than key, and the other - more"""
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
        """Merge takes as input two trees: left and right. To work correctly, the keys of the tree should be left less keys tree right.
         Here we take the top with the smallest key right wood the right and pull it up. After that, as the left subtree attach a tree left
         """
        if right is None:
            return left
        if left is None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    def add(self, root, key):
        """To add the key, use the split over it, and then make a new top of the root, which is the result of subtrees split"""
        left, right = self.split(root, key)
        root = Node(key, left, right)
        self.keep_parent(root)
        return root

    def remove(self, root, key):
        """To remove the top, you need to pick it up, and then merge its left and right subtrees"""
        root = self.find(root, key)
        self.set_parent(root.left, None)
        self.set_parent(root.right, None)
        return self.merge(root.left, root.right)

    def iterate(self):
        """No comments"""
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
            
            
    def contains(self, key):
        return self.find(self.root, key) == key

