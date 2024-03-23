class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        max_digit = 1
        for i in range(len(s)-1,-1,-1):
            if digits[s[i]] >= max_digit:
                res  += digits[s[i]]
                max_digit = digits[s[i]]
            else:
                res  -= digits[s[i]]
        return res
# 13.罗马数字转整数.py