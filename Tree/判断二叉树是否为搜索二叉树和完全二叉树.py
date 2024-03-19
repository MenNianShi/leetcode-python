# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root
# @return bool布尔型一维数组
#
class Solution:
    def judgeIt(self , root ):
        # write code here
        def judgeBST(root,low,high):
            if root==None:
                return True
            if root.val<=low or root.val>=high:
                return False
            return judgeBST(root.left,low,root.val) and judgeBST(root.right,root.val,high)
        def judgeBCT(root):
            res=[root]
            flag=0
            while res:
                tmp=res.pop(0)
                if tmp.left:
                    res.append(tmp.left)
                if tmp.right:
                    res.append(tmp.right)
                if tmp.right and not tmp.left:
                    return False
                if flag:
                    if tmp.left or tmp.right:
                        return False
                #左右节点都没有，或者只有左节点
                if (tmp.left and not tmp.right) or (not tmp.left and not tmp.right):
                    flag=1
            return True

        return [judgeBST(root,float('-inf'),float('inf')),judgeBCT(root)]
# 判断二叉树是否为搜索二叉树和完全二叉树.py