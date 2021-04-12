#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left!=None and root.left.left==None and root.left.right==None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cur = 0
        def dfs(is_left,root):
            if root!=None :
                if root.left==None and root.right ==None and is_left:
                    self.cur += root.val
                dfs(True,root.left)
                dfs(False,root.right)
        dfs(False,root)
        return self.cur