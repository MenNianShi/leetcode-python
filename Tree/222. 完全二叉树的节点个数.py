# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(root):
            depth = 0
            while root :
                depth+=1
                root = root.left # 完全二叉树只用算左边
            return depth
        cnt  = 0
        while root:
            left = getDepth(root.left) # 左子树深度
            right = getDepth(root.right) # 右子树深度
            if left == right: # 左右子树深度相同，左子树一定是满二叉树，右子树可能为满二叉树，一定为完全二叉树
                root = root.right
                cnt += 2 ** left
            else:  # 左右子树深度不同，右子树一定是满二叉树，左子树可能为满二叉树，一定为完全二叉树
                root = root.left
                cnt += 2**right
        return cnt