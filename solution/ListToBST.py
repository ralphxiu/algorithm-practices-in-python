#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def listToBST(alist):
    dummyHead = root = None
    length = len(alist)
    i = 0
    while i < length:
        if root == None:
            root = TreeNode(alist[i])
            i += 1
            continue
        elif root.left == None:
            root.left = TreeNode(alist[i])
            i += 1
            continue
        elif root.right == None:
            root.right = TreeNode(alist[i])
            i += 1
            continue
        else:
            root = root.left
