# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = set()
        for i in range(0,int(math.sqrt(c))+1):
            a.add(i**2)
        for j in a:
            if (c - j) in a:
                return True
        return False
a = Solution()
print(a.judgeSquareSum(5))
# 633.平方数之和  .py