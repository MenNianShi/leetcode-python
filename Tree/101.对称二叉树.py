# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3  判断二叉树是不是镜像对称的
import queue
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):#递归的方法
    # @param root, a tree node
    # @return a boolean
    def sym(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val == right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.sym(root.left, root.right)
from collections import deque
class Solution(object):#迭代方法
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lefts = deque([root.left])
        rights = deque([root.right])
        while lefts and rights:
            left = lefts.popleft()
            right = rights.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            lefts.extend([left.left, left.right])
            rights.extend([right.right, right.left])
        return True

# 101.对称二叉树.py