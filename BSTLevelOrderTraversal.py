#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.travel(root)

    def travel(self, root):
        if root == None:
            return []
        if root.left == root.right == None:
            return [[root.val]]
        else:
            leftChild = self.travel(root.left)
            rightChild = self.travel(root.right)

            long, short, minlen, maxlen = leftChild, rightChild, len(rightChild), len(leftChild) if len(
                leftChild) > len(rightChild) else long, short, maxlen = rightChild, leftChild, len(rightChild), len(
                rightChild)

            converge = [] * maxlen
            for i in range(minlen):
                converge[i] = long[i] + short[i]
            for i in range(minlen, maxlen):
                converge[i] = long[i]
            converge.append([root.val])
            return converge

