# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
#
#  
#
# 示例 1:
# 输入:
#
# "bbbab"
# 输出:
#
# 4
# 一个可能的最长回文子序列为 "bbbb"。
#
# 示例 2:
# 输入:
#
# "cbbd"
# 输出:
#
# 2

# dp 数组的定义是：在子串 s[i..j] 中，最长回文子序列的长度为 dp[i][j]。一定要记住这个定义才能理解算法。
#
# 为啥这个问题要这样定义二维的 dp 数组呢？我们前文多次提到，找状态转移需要归纳思维，说白了就是如何从已知的结果推出未知的部分，这样定义容易归纳，容易发现状态转移关系。
#
# 具体来说，如果我们想求 dp[i][j]，假设你知道了子问题 dp[i+1][j-1] 的结果（s[i+1..j-1] 中最长回文子序列的长度），你是否能想办法算出 dp[i][j] 的值（s[i..j] 中，最长回文子序列的长度）呢？
#
#
#
# 可以！这取决于 s[i] 和 s[j] 的字符：
#
# 如果它俩相等，那么它俩加上 s[i+1..j-1] 中的最长回文子序列就是 s[i..j] 的最长回文子序列：
#
#
#
# 如果它俩不相等，说明它俩不可能同时出现在 s[i..j] 的最长回文子序列中，那么把它俩分别加入 s[i+1..j-1] 中，看看哪个子串产生的回文子序列更长即可：
#

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        return dp[0][n-1]