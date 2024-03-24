# 102. 二叉树的层序遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        level = [root]
        while level:
            next_level = []
            vals = []
            for node in level:
                vals.append(node.val)
                if node.left:  next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
            ans.append(vals)
        return ans