
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides.sort(key = lambda r: r[1])
        m = len(rides)
        dp = [0] * (m+1)
        for i in range(m):
          j = bisect_right(rides,rides[i][0], hi=i, key=lambda r:r[1])
          dp[i+1] = max(dp[i], dp[j] + rides[i][1]-rides[i][0] + rides[i][2])
        return dp[m]
# 2008. 出租车的最大盈利.py