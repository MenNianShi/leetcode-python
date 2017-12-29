# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = str(x)
        sign = ''
        overflow = 2**31-1
        if tmp[0] == '-':
            sign = tmp[0]
            tmp = tmp[1:]
        res = tmp[::-1]
        for i in range(len(res)):
            if not res[i]==0:
                break
        res = res[i:]
        res = int(sign+res)
        if abs(res) > overflow:
            return 0
        else:
            return res
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) < 10:
            return x
        s = 0

        m = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            d = x % 10
            s = s * 10 + d
            x /= 10

        s = s * m
        return s if s < 2 ** 31 and s > -(2 ** 31) else 0
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        num = []

        if x < 0:
            sign = -1
        if x == 0:
            return 0
        x = abs(x)

        while x:
            num.append(x%10)
            x //= 10

        for i in num:
            res *= 10
            res += i

        if res > 0x7FffFFff:
            return 0
        else:
            return res * sign
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x<0 :
            s = s[1:]
            s = '-'+s[::-1]
        else:
            s = s[::-1]
        for i in range(0,len(s)):
            if s[i]==0:
                s = s[:i]+s[i+1:]
            else:
                break
        if int(s)>2**31 or int(s)<-2**31:
            return 0
        else:
            return int(s)



