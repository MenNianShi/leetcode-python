# 给定一个二叉树，我们在树的节点上安装摄像头。
#
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
#
# 计算监控树的所有节点所需的最小摄像头数量。
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 有三个状态:
# 0=>这个结点待覆盖
# 1=>这个结点已经覆盖
# 2=>这个结点上安装了相机
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def lrd(root):  # 后序 遍历
            if root == None:
                return 1
            left = lrd(root.left)
            right = lrd(root.right)
            if (left == 0 or right == 0):
                self.res += 1
                return 2
            if (left == 1 and right == 1):
                return 0
            return 1 # left+right >= 3:
        if (lrd(root)==0):
            self.res +=1
        return self.res


# 968. 监控二叉树.py