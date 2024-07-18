# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkHeight(root):
            if root is None:
                return 0

            leftHeight = checkHeight(root.left)
            if leftHeight == -1:
                return -1

            rightHeight = checkHeight(root.right)
            if rightHeight == -1:
                return -1

            heightDiff = abs(leftHeight - rightHeight)
            if heightDiff > 1:
                return -1
            else:
                return 1 + max(leftHeight, rightHeight)

        return checkHeight(root) != -1
