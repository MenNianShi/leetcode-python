# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        q = [root]
        is_odd = False
        while len(q) > 0:
            if is_odd:
                for i in range(len(q)//2):
                    nodex, nodey = q[i],q[len(q)-1-i]
                    nodex.val, nodey.val = nodey.val, nodex.val
            tmp = q
            q = []
            for node in tmp:
                if node.left is not None:
                    q.append(node.left)
                    q.append(node.right)
            # if is_odd:
            #     is_odd = False
            # else :
            #     is_odd = True
            is_odd ^= True
        return root