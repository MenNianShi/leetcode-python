class Solution(object):
    def minDistance(self, str1, str2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(str1)
        n = len(str2)
        #dp[i][j] 代表 str[:i] 转化到 str[:j]  的最小编辑距离
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,n+1):
            dp[0][i] = i
        for i in range(1,m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]+1
                    delete = dp[i-1][j]+1
                    replace = dp[i-1][j-1]+1
                    dp[i][j] = min(insert,delete,replace)
        return dp[m][n]
#带 插入/删除/替换权重的 编辑距离
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        # write code here
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,n+1):
            dp[0][i] = i*ic
        for i in range(1,m+1):
            dp[i][0] = i*dc
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]+ic
                    delete = dp[i-1][j]+dc
                    replace = dp[i-1][j-1]+rc
                    dp[i][j] = min(insert,delete,replace)
        return dp[m][n]
# 72. 编辑距离.py