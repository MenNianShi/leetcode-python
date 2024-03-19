
class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        res, dp = 0, 0
        for l in range(len(nums) - 1, -1, -1):
            if nums[l] > threshold:
                dp = 0
            elif l == len(nums) - 1 or nums[l] % 2 != nums[l + 1] % 2:
                dp = dp + 1
            else:
                dp = 1
            res = dp if nums[l] % 2 == 0 and dp > res else res
        return res




# 2760. 最长奇偶子数组.py