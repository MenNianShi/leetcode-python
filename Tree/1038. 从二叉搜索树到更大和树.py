# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        self.dfs(root, self.total)
        return root

    def dfs(self, root, right_sum):
        if root:
            self.dfs(root.right, self.total)
            self.total = root.val + self.total
            root.val = self.total
            self.dfs(root.left, self.total)

