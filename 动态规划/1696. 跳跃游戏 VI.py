class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = [0]
        for i in range(1, n):
            while queue and queue[0] < i - k:
                queue.pop(0)
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop(-1)
            queue.append(i)
        return dp[n - 1]
