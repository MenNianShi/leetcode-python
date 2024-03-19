# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 进阶:
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
#难点在于判断边界条件
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums)-1
        while nums[left] == nums[right] and left<right:
            left+=1
        while left<=right:
            mid =left + (right-left) //2
            if nums[mid] == target:
                return  True
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid+1
            else:
                if nums[mid] <= target<= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False
# 81. 搜索旋转排序数组 II.py