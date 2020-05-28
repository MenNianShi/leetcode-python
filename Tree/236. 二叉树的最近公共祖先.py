# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    parents= {}
    visited = set()
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.parents[root.val]=None
        self.dfs(root)
        while p!=None:
            self.visited.add(p.val)
            p = self.parents[p.val]
        while q!=None:
            if  q.val  in self.visited:
                return  q
            q = self.parents[q.val]

        return None

    def dfs(self, root):
        if root.left !=None:
            self.parents[root.left.val] = root
            self.dfs(root.left)
        if root.right !=None:
            self.parents[root.right.val] = root
            self.dfs(root.right)
a = TreeNode(2)
b =TreeNode(1)
d = TreeNode(2)
e = TreeNode(1)
a.left = None
a.right = b
c = Solution()
print(c.lowestCommonAncestor(a,d,e).val)

class Solution1(object):
    ans = TreeNode(0)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root,p,q)
        return self.ans
    def dfs(self,root,p,q):
        if root == None: return False
        lson = self.dfs(root.left,p,q)
        rson = self.dfs(root.right,p,q)
        if ((lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson))):
            self.ans = root
        return lson or rson or (root.val==p.val) or (root.val==q.val)



