class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 3 :
            return []
        nums.sort()
        if nums[0] > 0 :
                return res
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums) -1
            while left < right :
                if (nums[left] + nums[right] + nums[i] )== 0 :
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right  and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right  and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right] + nums[i]) > 0:
                    right -= 1
                else:
                    left += 1
        return res
