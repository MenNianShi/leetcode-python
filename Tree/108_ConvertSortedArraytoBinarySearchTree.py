# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, num):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(num)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(num[0])
        root = TreeNode(num[length / 2])
        root.left = self.sortedArrayToBST(num[:length / 2])
        root.right = self.sortedArrayToBST(num[length / 2 + 1:])
        return root
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = len(nums) / 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root
        return None