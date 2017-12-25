# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left and not right:
            return 1
        elif not left:
            return right + 1
        elif not right:
            return left + 1
        else:
            return min(left, right) + 1

#层次遍历，扫到哪层有叶子就返回层数
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [(root, 1)]

        while q:
            node, val = q.pop(0)
            if not node.left and not node.right:
                return val
            if node.left:
                q.append((node.left, val + 1))
            if node.right:
                q.append((node.right, val + 1))
