class Solution:
    def validMountainArray(self, A) :
        flag=0
        if len(A)<3 or A[0]>=A[1]:
            return False
        for i in range(len(A)-1):
            if flag==0:
                if A[i+1]<=A[i]:
                    flag=1
            if flag==1:
                if A[i+1]>=A[i]:
                    return False
        return flag==1

class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        p1 = 0
        p2 = 1
        fq = 0
        while p1 < p2 and p2 < len(A):
            if A[p1] < A[p2]:
                if fq==1:
                    return  False
                if p2 == len(A) - 1:
                    return False
                p1 += 1
                p2 += 1

            elif A[p1] == A[p2]:
                return False
            else:
                if p1 == 0:
                    return False
                if fq == 0:
                    max_num = A[p1]
                    fq = 1
                p1 += 1
                p2 += 1
        return True
A = Solution()
print(A.validMountainArray([0,3,2,1]))