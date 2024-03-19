# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True :
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k-1
            if k==0:
                return root.val
            root = root.right

# 230. 二叉搜索树中第K小的元素.py