class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for row in triangle:
            dp.append([float('inf')] * len(row))
        dp[0][0] = triangle[0][0]
        for i in range(1,len(dp)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])


class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]

        # 动态规划初始化，三角形左右边界值和顶点值
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        # 三角形中间值
        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        # print(dp)
        return min(dp[n - 1])
