class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(n-2,0,-2):
            ans += abs(cost[i]-cost[i+1])
            cost[i//2] += max(cost[i],cost[i+1])
        return ans
