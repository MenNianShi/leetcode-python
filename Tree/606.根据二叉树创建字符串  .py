# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t:
            s =str(t.val)
            print(s+'('+self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')')
        else:
            return
        return
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        ans = str(t.val)
        if t.left or t.right: ans += '(' + self.tree2str(t.left) + ')'
        if t.right: ans += '(' + self.tree2str(t.right) + ')'
        return ans

    def tree2str(self, t):#standard
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""

        node = str(t.val)

        if not t.left:
            if t.right:
                node += "()(" + self.tree2str(t.right) + ")"
        else:
            node += "(" + self.tree2str(t.left) + ")"
            if t.right:
                node += "(" + self.tree2str(t.right) + ")"

        return node
# 606.根据二叉树创建字符串  .py