# 设 dp[i][j] 为 A[i:] 和 B[j:] 的最长公共前缀，那么答案就为所有 dp[i][j] 中的最大值 max(dp[i][j])。
# 如果 A[i] == B[j]，那么状态转移方程为 dp[i][j] = dp[i + 1][j + 1] + 1，否则状态转移方程为 dp[i][j] = 0。

class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

