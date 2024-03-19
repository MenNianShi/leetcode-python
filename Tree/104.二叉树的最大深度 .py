# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxdepth = 0
        depth=0
        if root!=None:
            depth+=1
        else: return 0
        if depth>maxdepth:
            maxdepth =depth
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if l<= r:
            maxdepth = maxdepth+r
        else:
            maxdepth = maxdepth+l
        return maxdepth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# 104.二叉树的最大深度 .py