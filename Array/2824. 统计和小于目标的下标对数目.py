# 双指针
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        i,j = 0,len(nums) -1
        res = 0
        while i<j:
            while i < j and nums[i]+ nums[j] >= target:
                j-=1
            res += j-i
            i+=1
        return res