class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        tmp = 0
        ans = ""
        while tmp < len(s):
            ans += s[tmp:tmp + k][::-1]
            ans += s[tmp + k:tmp + k + k]
            tmp += 2 * k

        return ans

# 541.反转字符串 II .py