# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(nums)
        x = []
        for i in range(0,len(nums)):
            if l[i]!=nums[i]:
                x.append(i)
        if len(x)==0:
            return 0
        if len(x)==1:
            return 2
        if len(x)>1:
            return max(x)-min(x)+1

# 581.最短无序连续子数组  .py