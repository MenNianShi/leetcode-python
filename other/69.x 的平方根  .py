# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.
#
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
# Seen this question in a real interview before?  YesNo
import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        while low < high:
            mid = (low + high + 1) / 2
            if mid *mid <= x:
                low = mid
            else:
                high = mid - 1
        assert low == high
        return low

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
a = Solution()
print(a.mySqrt(8))
def newton_sqrt(n):
    eps = 0.0000001
    result = float(n)
    while True:
        lastvalue = result
        result = result-result/2.0+n/2.0/result
        if abs(result-lastvalue)<eps:
            break
    return result
print(newton_sqrt(4))
# 69.x 的平方根  .py