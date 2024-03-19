class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        #dp[i][j] 代表 str[:i] 转化到 str[:j]  的最小编辑距离
        for i in range(1,n+1):
            dp[0][i] = i
        for i in range(1,m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]+1
                    delete = dp[i-1][j]+1
                    replace = dp[i-1][j-1]+1
                    dp[i][j] = min(insert,delete,replace)
        return dp[-1][-1]
# 72. 编辑距离.py