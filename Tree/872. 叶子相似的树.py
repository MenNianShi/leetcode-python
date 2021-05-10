# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        a = self.preOrder(root1)
        b = self.preOrder(root2)
        return a==b
    def preOrder(self,root):
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur :
            while cur :
                if cur.left==None and cur.right==None:
                    res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res


class Solution:
    def leafSimilar(self, root1, root2):
        res1 = []
        res2 = []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return res1 == res2

    def dfs(self, root, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)


