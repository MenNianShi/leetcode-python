# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val==key:
            if root.left == None : return root.right
            if root.right == None: return root.left

            if root.left!=None and root.right!=None:
                minNode = self.getMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)

        if root.val> key :
            root.left = self.deleteNode(root.left,key)
        if root.val < key :
            root.right = self.deleteNode(root.right,key)
        return root
    def getMin(self,root):
        while root.left!=None:
            root = root.left
        return root