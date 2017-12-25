# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    count = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getDepth(root)
        return self.count00


    def getDepth(self,root):
        if root == None:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        temp = left + right
        if temp>self.count:
            self.count = temp
        return max(left,right)+1


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.s = 0
        self.dfs(root)
        return self.s

    def dfs(self, root):
        if not root: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.s = max(self.s, l + r)
        return max(l, r) + 1