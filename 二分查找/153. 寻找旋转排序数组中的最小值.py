# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
#



class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]
        # 找到数组的中间元素
        # mid。
        #
        # 如果中间元素 > 数组第一个元素，我们需要在
        # mid
        # 右边搜索变化点。
        #
        # 如果中间元素 < 数组第一个元素，我们需要在
        # mid
        # 做边搜索变化点。


        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1

class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left =0
        right = len(nums)-1
        result = float('inf')
        while left <= right:
            mid = left + (right-left)//2
            result = min(nums[mid],result)
            if nums[mid]>=nums[left]:
                if nums[left] <= nums[mid]<= nums[right]:
                    right = mid -1
                else:
                    left = mid+1
            else:
                right = mid -1
        return result