# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
#最长上升子序列
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        dp = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp += 1
            else:
                res = max(res, dp)
                dp = 1
        return max(res, dp)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        maxLength = 1
        count = 1
        for i in range(0,len(nums)):
            if i+1<len(nums) :
                if nums[i+1]>nums[i]:
                    count = count+1
                    if count>maxLength:
                        maxLength = count
                else:
                    count = 1
        return maxLength
a = Solution()
print(a.findLengthOfLCIS([2,2,2,2,2]))