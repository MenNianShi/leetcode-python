#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#

#求长度
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text2)
        m = len(text1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        if n == 0 or m == 0:
            return 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
#求内容
class Solution:
    def LCS(self, s1, s2):
        # write code here
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        direction = [[''] * (n + 1) for _ in range(m + 1)]
        if n == 0 or m == 0:
            return 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    direction[i][j] = 'ok'
                elif dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1]
                    direction[i][j] = 'left'
                else:
                    dp[i][j] = dp[i - 1][j]
                    direction[i][j] = 'up'
        s = []
        while dp[m][n]:
            c = direction[m][n]
            if c == 'ok':
                s.append(s1[m - 1])
                m -= 1
                n -= 1
            if c == 'left':
                n -= 1
            if c == 'up':
                m -= 1
        s = s[::-1]
        if len(s) == 0:
            return -1
        return ''.join(s)

# 最长公共子序列.py