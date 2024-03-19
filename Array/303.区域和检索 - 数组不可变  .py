# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>j or i>len(self.nums)-1 or j>len(self.nums)-1:
            return
        return sum(self.nums[i:j])

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] + [0] * len(nums)

        for i, num in enumerate(nums):
            self.nums[i + 1] = self.nums[i] + num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j + 1] - self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# 303.区域和检索 - 数组不可变  .py