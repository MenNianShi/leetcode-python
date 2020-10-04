# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left
            else:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right

        return root

