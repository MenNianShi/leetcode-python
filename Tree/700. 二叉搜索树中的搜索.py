# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left,val)
        if root.val < val:
            return self.searchBST(root.right,val)
# 700. 二叉搜索树中的搜索.py