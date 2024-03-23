class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        res = float('inf')
        flag = False
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= target:
                res = min(res, i - start + 1)
                flag = True
                cur_sum -= nums[start]
                start += 1
        return res if flag else 0



