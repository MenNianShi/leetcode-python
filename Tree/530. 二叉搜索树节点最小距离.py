# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    res, prev = float("inf"), float("-inf")
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res = min(self.res, root.val - self.prev)
            self.prev = root.val
            dfs(root.right)

        dfs(root)
        return self.res
class Solution(object):
    def getMinimumDifference(self, root): #由于是二叉查找树，中序遍历，取两两间最小值即可
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root, l=[]):
            if root.left:
                inorder(root.left, l)
            l.append(root.val)
            if root.right:
                inorder(root.right, l)
            return l
        l = inorder(root, [])
        return min([l[i + 1] - l[i] for i in range(len(l) - 1)])




# 530. 二叉搜索树节点最小距离.py