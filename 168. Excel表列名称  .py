# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#就是将一个数转化为26进制
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''

        while n:
            res = chr((n-1)%26 + 65) + res
            n = (n-1) // 26
        return res
a = Solution()
print(a.convertToTitle(27))
