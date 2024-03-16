# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        if n <= 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:root_index+1] , inorder[:root_index])
            root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root