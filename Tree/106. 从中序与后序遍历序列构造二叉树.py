# 106. 从中序与后序遍历序列构造二叉树
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        if n == 0 :
            return None
        root  = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1]) # 左子树个数

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        return  root

