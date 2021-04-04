# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# 卡塔兰数
# 题目要求是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：
#
# G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数。
#
# F(i, n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 (1 \leq i \leq n)(1≤i≤n)。
#
# 可见，G(n) 是我们求解需要的函数。
#
# 稍后我们将看到，G(n)G可以从 F(i, n) 得到，而 F(i, n) 又会递归地依赖于 G(n)。


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

