class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key


class SplayTree(object):
    def __init__(self):
        self.root = None
        self.header = Node(None)  # For splay()

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise Exception('key not found in tree')

        # Now delete the root.
        if self.root.left is None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def find_min(self):
        if self.root is None:
            return None
        x = self.root
        while x.left is not None:
            x = x.left
        self.splay(x.key)
        return x.key

    def find_max(self):
        if self.root is None:
            return None
        x = self.root
        while x.right is not None:
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root is None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def is_empty(self):
        return self.root is None

    def splay(self, key):
        left = right = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if not t.left:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if not t.left:
                        break
                right.left = t
                right = t
                t = t.left
            elif key > t.key:
                if not t.right:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if not t.right:
                        break
                left.right = t
                left = t
                t = t.right
            else:
                break
        left.right = t.left
        right.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

