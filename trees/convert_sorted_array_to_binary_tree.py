# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


# Test the function
nums = [-10, -3, 0, 5, 9]
nums1 = [1, 3]
solution = Solution()
bstRoot = solution.sortedArrayToBST(nums)
bstRoot1 = solution.sortedArrayToBST(nums1)
print(inorderTraversal(bstRoot))  # Output should be [-10, -3, 0, 5, 9]
print(inorderTraversal(bstRoot1))  # Output should be [1, 3]