# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        for x in range(1, size / 2 + 1):
            if size % x:
                continue
            if str[:x] * (size / x) == str:
                return True
        return False
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = s + s
        i = new_s.find(s, 1)
        if i < len(s):
            return True
        return False
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
# 459.重复的子字符串.py