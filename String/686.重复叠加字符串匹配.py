class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for c in B:
            if c not in A:
                return -1
        q=(len(B)-1)/len(A)+1
        for i in range(2):
            if B in A*(q+i):
                return q+i
        return -1
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        k = (n-1) // m + 1
        if B in A*k:
            return k
        elif B in A*(k+1):
            return k+1
        else:
            return -1
print(1//5)
a = Solution()
print(a.repeatedStringMatch('aaaa','aaaaaaaaa'))
# 686.重复叠加字符串匹配.py