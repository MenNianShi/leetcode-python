class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            start = i
            i+=1
            while i < n and nums[i] - nums[i-1] == 1 :
                i+=1
            end = i - 1
            temp = str(nums[start])
            if start < end:
                temp += "->" + str(nums[end])
            res.append(temp )
        return res


# 228 汇总区间