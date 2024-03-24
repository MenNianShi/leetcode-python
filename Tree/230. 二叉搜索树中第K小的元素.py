class Solution:
    def kthSmallest(self, root, k) :
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = self.inorder(root)
        return arr[k - 1]

    def inorder(self, root):
        if root == None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

# 230. 二叉搜索树中第K小的元素.py