# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, cur_sum, list_temp): # 不需要self
            if root.left == None and root.right == None:
                if cur_sum == sum:
                    return list_all.append(list_temp)
            if root.left:
                dfs(root.left, cur_sum + root.left.val, list_temp + [root.left.val])
            if root.right:
                dfs(root.right, cur_sum + root.right.val, list_temp + [root.right.val])
        if root == None:
            return []
        list_all = []
        dfs(root, root.val, [root.val])
        return list_all


class Solution:
    def pathSum(self, root, total) :
        ret = list()
        path = list()

        def dfs(root, total):
            if not root:
                return
            path.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path[:])
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()

        dfs(root, total)
        return ret








# 113. 路径总和 II.py