# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.preprocess(s)
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    def preprocess(self, s):
        res = ''
        for c in s:
            c = c.lower()
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) or  (ord('9')>=ord(c)>=ord('0')):
                res += c
        return res
# 125.合法回文串.py