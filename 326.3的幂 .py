#判断一个数是否为3的幂次，不用循环和递归
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (1162261467 % n == 0)

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        tmp = math.log(n, 3)
        return 3 ** round(tmp, 0) == n

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = math.log(n, 2)
        return 2 ** round(x, 0) == n
