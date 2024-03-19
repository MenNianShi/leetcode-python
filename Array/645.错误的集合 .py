#找出数组1-n中，出现两次和没出现的
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        twice = sum(nums) - sum(set(nums))
        miss = twice + n*(n+1)/2 - sum(nums)
        return [twice, miss]
# 645.错误的集合 .py