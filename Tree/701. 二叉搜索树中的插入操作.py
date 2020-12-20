# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        if root.val< val:
            root.right =  self.insertIntoBST(root.right,val)
        return root