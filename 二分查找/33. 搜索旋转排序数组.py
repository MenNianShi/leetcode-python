# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <=high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[high]:
                if nums[mid]< target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low =mid +1
        return  -1



a = Solution()
print(a.search([1],0))
# 33. 搜索旋转排序数组.py