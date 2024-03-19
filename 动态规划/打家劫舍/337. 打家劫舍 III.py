# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    memo = {}   # 利用备忘录消除重叠子问题
    def rob(self, root):
        if root == None:
            return 0
        if root in self.memo:
            return self.memo[root]
        # 抢当前，去下下家
        do = root.val + (self.rob(root.left.left)+self.rob(root.left.right) if root.left else 0 ) + (self.rob(root.right.left)+self.rob(root.right.right) if root.right else 0 )
        # 不抢当前 去下家
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do,not_do)
        self.memo[root] = res
        return  res
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dp(root):
            if root != None:
                left = dp(root.left)
                right = dp(root.right)

                do = root.val + left[0] + right[0]
                not_do = max(left) + max(right)

                return not_do, do
            else:
                return 0, 0

        return max(dp(root))
# 337. 打家劫舍 III.py