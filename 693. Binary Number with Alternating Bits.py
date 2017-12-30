# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
print(bin(3))
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        for i in xrange(1, len(b)):
            if b[i] == b[i-1]:
                return False
        return True
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = str(bin(n))[2:]
        if len(m)==2:
            return m[0]!=m[1]
        if len(m)==1:
            return True
        for i in range(1,len(m)-1):
            if m[i]==m[i-1] or m[i]==m[i+1]:
                return False
        return True