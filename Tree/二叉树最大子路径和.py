class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    max_sum = float('-inf')
    def getMaxPathSum(self,root):
        def dfs(root):
            if root == None :
                return 0
            left  = dfs(root)
            right = dfs(root)
            cur_sum = max(root.val,root.val+max(left,right))

            self.max_sum = max(self.max_sum,left+right+root.val, cur_sum)
            return cur_sum
        dfs(root)
        return self.max_sum