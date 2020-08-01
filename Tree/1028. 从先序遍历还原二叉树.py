# 我们从二叉树的根节点 root 开始进行深度优先搜索。
#
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
#
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
#
# 给出遍历输出 S，还原树并返回其根节点 root。
#
#  
#
# 示例 1：
#
#
#
# 输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S) :
        def part(s):
            STATE_DEPTH = 1
            STATE_NUM = 2
            depth = 0
            num = 0
            state = STATE_DEPTH
            for i in s + '$':
                #print(i, state)
                if state == STATE_DEPTH:
                    if i == '-':
                        depth += 1
                    elif i in '0123456789':
                        state = STATE_NUM
                        num = ord(i) - 48
                elif state == STATE_NUM:
                    if i in '-$':
                        yield (depth, num)
                        state = STATE_DEPTH
                        depth = 1
                        num = 0
                    elif i in '0123456789':
                        num = num * 10 + ord(i) - 48
        t = {}
        for d, n in part(S):
            #print(d, n)
            t[d] = TreeNode(n)
            if d > 0:
                parent = t[d - 1]
                if parent.left is None:
                    parent.left = t[d]
                else:
                    parent.right = t[d]
        return t[0] if t else None
