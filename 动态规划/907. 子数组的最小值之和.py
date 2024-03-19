# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
#
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
# 单调栈 动态规划
mod = 10 ** 9 + 7
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        monostack = []
        dp = [0] * n
        ans = 0
        for i, x in enumerate(arr):
            while monostack and arr[monostack[-1]] > x:
                monostack.pop()
            k = i- monostack[-1] if monostack else i+1
            dp[i] = k * x + (dp[i-k] if monostack else 0)
            ans = (ans + dp[i]) % mod
            monostack.append(i)
        return ans

# 907. 子数组的最小值之和.py