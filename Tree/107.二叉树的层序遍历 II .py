# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
 #Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = []
        cur = [root]
        while (len(cur) > 0):
            next_level = []
            level_val = []
            for node in cur:
                level_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur = next_level
            level.append(level_val)
        return level[::-1]


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 最终结果
        res = []
        # 存放每一层结果
        levelRes = []

        if root == None:
            return res

            # 当前一层的节点
        current = []
        # 下一层的节点
        next = []

        # 根节点加入
        current.append(root)

        while len(current) > 0:

            # 弹出第一个元素
            node = current.pop(0)

            if node.left != None:
                next.append(node.left)

            if node.right != None:
                next.append(node.right)

                # 加入访问节点的值
            levelRes.append(node.val)

            if len(current) == 0:
                current = next
                next = []
                res.append(levelRes)
                levelRes = []

        res.reverse()
        return res