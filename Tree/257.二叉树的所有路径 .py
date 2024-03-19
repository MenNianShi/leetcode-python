#给出从根到每个结点的路径
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res,path_list=[],[]
        self.dfs(root,path_list,res)
        return res
    def dfs(self,root,path_list,res):
        if not root:
            return
        path_list.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path_list))
        if root.left:
            self.dfs(root.left,path_list,res)
        if root.right:
            self.dfs(root.right,path_list,res)
        path_list.pop()#返回从列表中移除的元素对象。默认是最后一个


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        path, paths = "", []
        self.dfs(root, path, paths)
        return paths

    def dfs(self, node, path, paths):
        if not path:
            path += str(node.val)
        else:
            path += "->" + str(node.val)
        if not node.left and not node.right:
            paths.append(path)
        else:
            if node.left:
                self.dfs(node.left, path, paths)
            if node.right:
                self.dfs(node.right, path, paths)
# 257.二叉树的所有路径 .py