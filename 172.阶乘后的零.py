# Given an integer n, return the number of trailing zeroes in n!.
#返回n的阶乘尾部0的个数
import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n/5
            res += n
        return res