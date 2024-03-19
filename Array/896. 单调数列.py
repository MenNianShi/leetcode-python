# 如果数组是单调递增或单调递减的，那么它是单调的。
#
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
#
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
#一次遍历

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        asc = True
        desc = True
        if len(A)<=1:
            return True
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                desc = False
            if A[i]< A[i-1]:
                asc = False
        return asc or desc
# 896. 单调数列.py