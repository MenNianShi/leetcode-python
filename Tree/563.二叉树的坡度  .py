# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    sum = 0
    def helper(self,root):
        if root==None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.sum +=abs(left-right)
        return root.val+left+right

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.sum


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def find(root):
            if not root:
                return 0

            left = find(root.left)
            right = find(root.right)
            self.res += abs(left - right)
            return left + right + root.val

        find(root)

        return self.res
# 563.二叉树的坡度  .py