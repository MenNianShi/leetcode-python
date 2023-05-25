#动态规划 同494。目标和
# 定义二维布尔数组 dp，其中dp[i+1][j] 表示前 ii 个石头能否凑出重量 jj。特别地，dp[0][] 为不选任何石头的状态，因此除了
# dp[0][0] 为真，其余 dp[0][j] 全为假。
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        n ,m= len(stones),total//2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0]=True
        for i in range(n):
            for j in range(m + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]

        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break

        return ans

