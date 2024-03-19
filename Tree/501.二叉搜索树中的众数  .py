# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 使用中序遍历。BST 的中序遍历结果是有序的。
# 遍历两次。第一次确定结果集的大小，第二次得到结果集。
class Solution:
    def __init__(self):
        self.pre = None
        self.ret = []
        self.ret_count, self.max_count, self.cur_count = 0, 0, 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        self.pre = None
        self.ret = [0] * self.ret_count
        self.ret_count, self.cur_count = 0, 0
        self.inOrder(root)
        return self.ret

    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.ret_count = 1
        elif self.cur_count == self.max_count:
            if len(self.ret):
                self.ret[self.ret_count] = root.val
            self.ret_count += 1
        self.pre = root
        self.inOrder(root.right)

# 501.二叉搜索树中的众数  .py