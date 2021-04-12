# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
class Solution(object):
    def validPalindrome(self, s):
        rev = s[::-1]
        if s == rev:
            return True
        l = len(s)
        for i in xrange(l):
            if s[i] != rev[i]:
                return s[i:l-i-1] == rev[i+1:l-i] or rev[i:l-i-1] == s[i+1:l-i]
        return False
a = Solution()
print(a.validPalindrome('abca'))