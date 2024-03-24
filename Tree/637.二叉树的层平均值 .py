# Definition for a binary tree node.

import queue
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        res = []
        level = [root]
        while len(level)>0:
            cur_level = []
            next_level = []
            for node in level:
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append((sum(cur_level)*1.0)/len(cur_level))
            level = next_level
        return res
# 637.二叉树的层平均值 .py