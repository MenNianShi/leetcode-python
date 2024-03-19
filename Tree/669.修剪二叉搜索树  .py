# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L).
# You might need to change the root of the tree,
# so the result should return the new root of the trimmed binary search tree.
#
# Example 1:
# Input:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output:
#     1
#       \
#        2
# Example 2:
# Input:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output:
#       3
#      /
#    2
#   /
#  1
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
# 当root的值位于L和R之间，则递归修剪其左右子树，返回root。
# 当root的值小于L，则其左子树的值都小于L，抛弃左子树，返回修剪过的右子树。
# 当root的值大于R，则其右子树的值都大于R，抛弃右子树，返回修剪过的左子树。
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root ==None:
            return
        if root.val<L:
            return self.trimBST(root.right,L,R)
        elif root.val>R:
            return self.trimBST(root.left,L,R)
        else:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
            return root

# 669.修剪二叉搜索树  .py