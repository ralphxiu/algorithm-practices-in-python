class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, start, new_val):
        if new_val < start.value:
            if start.left:
                self.insert_helper(start.left, new_val)
            else:
                start.left = Node(new_val)
        if new_val > start.value:
            if start.right:
                self.insert_helper(start.right, new_val)
            else:
                start.right = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, start, find_val):
        if not start:
            return False
        elif start.value == find_val:
            return True
        else:
            return self.search_helper(start.left, find_val) if start.value < find_val else self.search_helper(
                start.right, find_val)

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def print_tree(self):
        print("pre-order: " + self.preorder_print(self.root, "")[:-1])
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.print_tree()
# Check search
# Should be True
print(tree.search(4))

# Should be False
print(tree.search(6))
