# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        preSum = 0
        res = 0
        for  num in nums:
            preSum +=num
            if (preSum-k) in d:
                res+=d[preSum-k]
            if preSum not in d:
                d[preSum]=1
            else:
                d[preSum]+=1
        return res
