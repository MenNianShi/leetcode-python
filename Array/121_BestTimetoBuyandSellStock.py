def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxprofit = 0
    for i in range(0, len(prices)):
        if i+1<len(prices):
            a = max(prices[i+1:])
            profit = a-prices[i]
        if profit>maxprofit:
            maxprofit = profit
    return maxprofit
print(maxProfit([1]))
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        MAX = 0

        start = prices[0]

        for price in prices:
            if price - start > MAX:
                MAX = price - start
            if price < start :
                start = price

        return MAX