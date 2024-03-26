class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        cur = 0
        num = x
        while num != 0 :
            cur = cur * 10 + num%10
            num = num//10
        return cur == x
# 9.回文数 .py