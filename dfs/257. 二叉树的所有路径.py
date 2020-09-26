# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(root,cur):
            if root:
                if root.left == None and root.right== None:
                    res.append(cur+str(root.val))
                else:
                    dfs(root.left,cur+str(root.val)+"->")
                    dfs(root.right,cur+str(root.val)+"->")
        dfs(root,"")
        return res