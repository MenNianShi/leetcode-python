#给一个无符号数，求其二进制中1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count
class Solution(object):
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, max):
        n, a, b = 0, 0, 1
        if max == 1:
            return 0
        if max == 2:
            return 1
        while n < max-2:
            a, b = b, a + b
            n = n + 1
        return b
a = Solution()
print(a.fibonacci(6))