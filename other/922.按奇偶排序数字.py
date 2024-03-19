class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        j = 1
        i = 0
        while i< n:
            if A[i]%2==1:
                while A[j]%2==1:
                    j+=2
                A[i],A[j]=A[j],A[i]
            i+=2
        return A


# 922.按奇偶排序数字.py