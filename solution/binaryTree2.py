class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, x):
        self.root = TreeNode(x=0)

    def addNode(self, x):

