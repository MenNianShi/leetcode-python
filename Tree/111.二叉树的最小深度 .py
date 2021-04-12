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
        if root !=None:
            if root.left==None and root.right==None:
                return 1
            elif root.left!=None and root.right==None:# 保证 是叶子节点
                return 1+self.minDepth(root.left)
            elif root.left==None and root.right!=None:# 保证 是叶子节点
                return 1+self.minDepth(root.right)
            else:
                return 1+ min(self.minDepth(root.left),self.minDepth(root.right) )
        else:
            return 0

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
