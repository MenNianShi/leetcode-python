# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        if n<=0:
            return  0
        max_k = 2
        # 定义三维数组，第i天、交易了多少次、当前的买卖状态
        dp = [[[0,0] for _ in range(max_k+1)] for _ in range(n)]
        # 初始化第一天，这里的dp[0][2][1]可以不用管，后面也不会用到
        for k in range(0,max_k+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(1,n):
            # 第一次买卖
            for j in range(1,max_k+1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j-1][0] - prices[i])

        return dp[-1][2][0]