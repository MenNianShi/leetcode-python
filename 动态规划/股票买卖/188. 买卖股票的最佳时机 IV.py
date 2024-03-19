# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1：
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
class Solution(object):
    def maxProfit_inf(self, prices):
        n = len(prices)
        if n <= 0:
            return 0
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):

            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 0:
            return 0
        if (K > n / 2):
            return self.maxProfit_inf(prices);
        dp = [[[0, 0] for _ in range(K + 1)] for _ in range(n)]
        for i in range(K + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, K + 1):
                # 处理第k次买入
                dp[i][j - 1][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0] - prices[i])
                # 处理第k次卖出
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
        return dp[n - 1][K][0]
# 188. 买卖股票的最佳时机 IV.py