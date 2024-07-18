# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
      if not root:
        return True
      
      def isSame(node1, node2):
        if not node1 and not node2:
          return True
        if not node1 or not node2:
          return False
        return (node1.val == node2.val) and isSame(node1.left, node2.right) and isSame(node1.right, node2.left)
      
      return isSame(root.left, root.right)
