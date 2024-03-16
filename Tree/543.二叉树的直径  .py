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
    res = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getdepth(root)
        return self.res
    def getdepth(self, root):
        if root ==None:
            return 0
        else:
            # 求当前节点的左右子树深度
            leftdepth = self.getdepth(root.left)
            rightdepth = self.getdepth(root.right)
            cur = leftdepth + rightdepth + 1
            self.res = max(self.res, cur - 1) # 直径 = 深度 - 1
            return max(leftdepth , rightdepth) + 1 # 深度 = 子树深度 + 1