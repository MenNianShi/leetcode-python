# Definition for a binary tree node.
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
#
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
#
# 返回森林中的每棵树。你可以按任意顺序组织答案。

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []

        def dfs(root):
            if root == None: return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if (root != None and root.val in to_delete):
                if root.left != None: res.append(root.left)
                if root.right != None: res.append(root.right)
                return None
            return root

        if (dfs(root) != None):
            res.append(root)
        return res

# 1110. 删点成林.py