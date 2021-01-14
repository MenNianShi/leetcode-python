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
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        res.append(self.bin_left(nums,target))
        res.append(self.bin_right(nums,target))
        return res
    def bin_left(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+ (right-left)//2
            if nums[mid]==target:
                right = mid-1
            elif nums[mid]>target:
                right= mid-1
            else:
                left = mid +1
        if left >=len(nums) or nums[left]!=target:
            return -1
        return left
    def bin_right(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+ (right-left)//2
            if nums[mid]==target:
                left = mid+1
            elif nums[mid]>target:
                right= mid-1
            else:
                left = mid +1
        if right < 0 or nums[right]!=target:
            return -1
        return right

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = self.binsearch(nums,target)
        if x ==-1:
            return [-1,-1]
        else:
            left=x
            right =x
            while left-1>=0:
                if nums[left-1]==target:
                    left = left-1
                else:
                    break
            while right+1<len(nums):
                if nums[right+1]==target:
                    right= right+1
                else:
                    break
            return [left,right]

    def binsearch(self,nums,target):
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1