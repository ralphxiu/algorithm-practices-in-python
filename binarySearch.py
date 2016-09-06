class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)
        # return False

    def print_tree(self):
        print("pre-order: " + self.preorder_print(self.root, "")[:-1])
        print("in-order: " + self.inorder_print(self.root, "")[:-1])
        print("post-order: " + self.postorder_print(self.root, "")[:-1])

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start.value == find_val:
            return True
        elif start.left:
            return self.preorder_search(start.left, find_val)
        elif start.right:
            return self.preorder_search(start.right, find_val)
        else:
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            if start.left:
                traversal = self.postorder_print(start.left, traversal)
            if start.right:
                traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
tree.print_tree()