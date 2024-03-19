# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# 判断给定的序列是否可以最多只改变一个数字就能得到非递减序列。
# 主要难点是分析所有可能的情况，程序必须要知道最小改动的数字位置是什么地方。
# 当遇到递减的情况（A[i]< A[i-1]）时需要进行修改，但是存在两种情况，1）改动A[i]，2）改动A[i-1]。
# 如果A[i-2]<=A[i]，则改动A[i]，否则改动A[i-1]，这样不会影响后面数据的判断。

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True
        flag = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if flag == 0:
                    return False
                if i == 1 or nums[i - 2] < nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                flag -= 1
        return True


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        times = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                times += 1
                if times == 2:
                    return False
                if (i != 1 and i != len(nums) - 1):
                    if (nums[i - 1] > nums[i + 1] and nums[i] < nums[i - 2]):
                        return False
        return True


# 665.非递减数列  .py