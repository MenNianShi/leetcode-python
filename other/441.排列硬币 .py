# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    i=1
    while i+(i*(i-1)) / 2 <= n:
        i=i+1
    return i-1
print(arrangeCoins(5))
#解一元二次方程：x^2 + x = 2 * n 解得：x = sqrt(2 * n + 1 / 4) - 1 /2
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        order = sqrt(2.0 * floor(n) + 0.25) - 0.5
        return int(order)
# 441.排列硬币 .py