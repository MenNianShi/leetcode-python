class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2 :
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1+n2+1)//2
        left = 0
        right = n1
        while left <right:
            m1 = left+(right-left)//2#m1 为 数组1 右半边最小值 下标
            m2 = k-m1  #m2-1 为数组2 左半边最大值 下标
            if nums1[m1]<nums2[m2-1]:# 数组1右半边 最小值 < 数组2左半边最大值
                left = m1+1 #这一行才是精髓
            else:
                right =m1
        m1 = left
        m2 = k-m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2.0
a = [1,2]
b = [3,4]
c = Solution()
print(c.findMedianSortedArrays(a,b))