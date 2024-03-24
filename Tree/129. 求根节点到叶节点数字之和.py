# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root,0)

    def helper(self,root,cur_val):
        if root == None:
            return 0
        cur_val = cur_val* 10 + root.val
        if root.left == None and root.right == None:
            return cur_val
        return self.helper(root.left,cur_val) + self.helper(root.right,cur_val)

