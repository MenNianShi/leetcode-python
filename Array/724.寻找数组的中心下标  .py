# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
#
# Example 1:
# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:
# Input:
# nums = [1, 2, 3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)

        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = sum(nums)
        total = 0
        for x, n in enumerate(nums):
            if sums - n == 2 * total: return x
            total += n
        return -1
a = Solution()
print(a.pivotIndex([-1,-1,-1,-1,-1,-1]))
# 724.寻找数组的中心下标  .py