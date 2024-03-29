# Definition for a binary tree node.
# 判断是否为二叉搜索树
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.dfs(root, None, None)
    def dfs(self, root, minNode, maxNode):
        # 左右子树的val 在 上下限 之间，递归更新上下限
        if root == None:
            return True
        if minNode!= None and  root.val <= minNode.val:
            return False
        if maxNode!=None and root.val  >= maxNode.val:
            return False
        return self.dfs(root.left, minNode, root) and self.dfs(root.right, root,maxNode)


# 98. 验证二叉搜索树.py