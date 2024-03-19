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
        #dp[i][j] 表示 text1[:i] 与 text2[:j]  最长公共子序列长度
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
# 1143.最长公共子序列