# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        left = 0
        right = 2
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                right += 1
            else:

                nums.pop(right)

        return len(nums)
# 80. 删除有序数组中的重复项 II.py