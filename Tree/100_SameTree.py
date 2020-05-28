# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

b = TreeNode(3)
c = TreeNode(9)
d = TreeNode(20)
e = TreeNode(15)
f = TreeNode(7)
b.left = c
b.right = d
d.left = e
d.right =f
x = b
y=b
a = Solution()
print(a.isSameTree(x,y))
