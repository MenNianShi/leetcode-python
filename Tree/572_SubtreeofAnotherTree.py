# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s==None : return False
        if self.isSame(s,t) : return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    def isSame(self,s,t):
        if s==None and t==None:
            return True
        if s==None or t==None:
            return False
        if s.val!=t.val : return False
        return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def preorder(node):
            if node is None:
                return "%"
            return "*" + str(node.val) + "#" + preorder(node.left) + preorder(node.right)

        return preorder(t) in preorder(s)


class Solution(object):
    def isSubtree(self, s, t, sub=False):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s is None and t is not None:
            return False
        elif s is not None and t is None and sub:
            return False
        elif t is None:
            return True

        if s.val == t.val:
            return (self.isSubtree(s.right, t.right, True) and self.isSubtree(s.left, t.left, True)) or self.isSubtree(
                s.right, t) or self.isSubtree(s.left, t)
        else:
            if sub:
                return False
            else:
                return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)