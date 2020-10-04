# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
#
# 示例 1：
#
# 输入：leaves = "rrryyyrryyyrr"
#
# 输出：2
#
# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
#
#f[i][j] 表示对于第 0 片到第 i 片 叶子进行调整操作，并且第 i 片叶子处于状态 j 时的最小操作次数。

class Solution:
    def minimumOperations(self, leaves) :
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = int(leaves[0] == "y")
        f[0][1] = f[0][2] = f[1][2] = float("inf")

        for i in range(1, n):
            isRed = int(leaves[i] == "r")
            isYellow = int(leaves[i] == "y")
            f[i][0] = f[i - 1][0] + isYellow # 当前是黄叶子就需要 再调换一次
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + isRed # 当前是红叶子，就需要调换1次
            if i >= 2:# 至少3个叶子
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + isYellow

        return f[n - 1][2]

