# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    maxsum = 0
    for i in range(0,len(nums)):
        if i+k<=len(nums) and sum(nums[i:i+k])> maxsum :
            maxsum = sum(nums[i:i+k])
    return maxsum/k
print(findMaxAverage([0,1,1,3,3],4))
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        curSum = 0
        addNum = 0
        for i in range(0, len(nums)):
            if addNum < k:
                curSum += nums[i]
                sum = curSum
                addNum += 1
            else:
                curSum = curSum - nums[i - k] + nums[i]
                sum = max(sum, curSum)
        return sum * 1.0 / k
# 643.子数组最大平均数 I  .py