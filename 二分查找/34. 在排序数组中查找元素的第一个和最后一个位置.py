# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6

class Solution(object):
    def binsearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right :
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = self.binsearch(nums,target)
        if index == -1:
            return [-1,-1]
        left_index = index
        right_index = index
        while left_index >=0 and nums[left_index] == target:
            left_index -= 1
        while right_index <= len(nums)-1 and nums[right_index] == target:
            right_index+=1
        return [left_index+1,right_index-1]



# 34. 在排序数组中查找元素的第一个和最后一个位置.py