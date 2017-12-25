# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        elif p!=None and q!=None and p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
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
