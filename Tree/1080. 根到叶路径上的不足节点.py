
# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
#
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
#
# 叶子节点，就是没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#删除所有路径和小于limit的路径 反过来的意思就是 保留所有路径和大于等于limit的路径
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        # 如果节点为空直接返回即可
        if root == None:
            return root
        # 如果当前节点为叶子节点
        if (root.left == None and root.right == None):
            # 大于limit直接返回
            if (root.val >= limit):
                return root
            #  小于limit  返回空节点 即代表删除这个节点
            else:
                return None
        # 非叶子节点，递归它的左右子节点
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        # 如果递归后左右子节点为空，就代表经过它的路径都是小于limit，那么这个节点都可以删除了
        if (root.left == None and root.right == None):
            return None
        else:
            return root

# 1080. 根到叶路径上的不足节点.py