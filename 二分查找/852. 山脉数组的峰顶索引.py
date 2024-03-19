class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A)-1
        while left<=right:
            mid = left+ (right-left)//2
            if A[mid]<A[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return left

a = Solution()
print(a.peakIndexInMountainArray([3,4,5,1]))
# 852. 山脉数组的峰顶索引.py