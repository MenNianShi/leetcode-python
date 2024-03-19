# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
#  
#
# 示例 2:
#
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
class Solution(object):
    def binsearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid -1
            else:
                left = mid+1
        return left

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x < arr[0]: return arr[:k]
        elif x > arr[-1] : return arr[-k:]
        else:
            pivot = max(self.binsearch(arr,x),0)
            low = max(pivot -k-1,0)
            high = min(pivot+k-1,len(arr)-1)
            while high-low > k-1:
                if abs(arr[high]-x) >= abs(arr[low]-x):
                    high-=1
                else:
                    low+=1
            return arr[low:high+1]





a = Solution()
print(a.findClosestElements([1,1,1,10,10,10],1,9))


# 658. 找到 K 个最接近的元素.py