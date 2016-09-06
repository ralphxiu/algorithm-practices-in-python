# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        pathLeft = 0
        pathRight = 0
        if root.left:
            pathLeft = 1 + self.maxDepth(root.left)
        if root.right:
            pathRight = 1 + self.maxDepth(root.right)
        path = max(pathLeft, pathRight, 1)
        return path

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

print(s.maxDepth(root))


