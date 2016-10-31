# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        def findLeftLeaves(node, isLeft):
            sum = 0
            if isLeft and node.left == None and node.right == None:
                sum += node.val
            if node.left:
                sum += findLeftLeaves(node.left, True)
            if node.right:
                sum += findLeftLeaves(node.right, False)
            return sum

        return findLeftLeaves(root, False)