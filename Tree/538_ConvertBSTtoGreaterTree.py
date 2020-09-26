# Definition for a binary tree node.
#这题就是说对每个节点，加上所有比它大的值。
# 说简单也简单，关键在于二分查找树。
# 利用二分查找树的特性，我们可以很容易得出从大到小的数组序列，即中序遍历（右子树-根节点-左子树）
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    sum = 0
    def convert(self,root):
        if root==None: return
        self.convert(root.right)
        self.sum += root.val
        root.val=self.sum

        self.convert(root.left)
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root,self.sum)
        return root
class Solution(object):

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.node_sum = 0
        def convert(root):
            if root==None:return
            convert(root.right)
            self.node_sum += root.val
            root.val = self.node_sum
            convert(root.left)
        convert(root)
        return root
