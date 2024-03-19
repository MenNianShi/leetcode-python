# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def buildtrees(start,end):
            if (start>end):
                return[None,]
            all_trees = []
            for i in range(start,end+1):
                left_trees = buildtrees(start,i-1)
                right_trees = buildtrees(i+1,end)

                for l in left_trees:
                    for r in right_trees :
                        temp = TreeNode(i)
                        temp.left = l
                        temp.right = r
                        all_trees.append(temp)
            return all_trees
        return buildtrees(1,n)
# 95. 不同的二叉搜索树 II.py