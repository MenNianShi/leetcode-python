# 103. 二叉树的锯齿形层序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        level = [root]
        is_zig = True
        while level:
            next_level = []
            vals = []
            for node in level:
                vals.append(node.val)
                if node.left:  next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
            if is_zig:
                ans.append(vals)
            else:
                ans.append(vals[::-1])
            is_zig = not is_zig
        return ans
