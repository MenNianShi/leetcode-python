# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                s = s[0:i]
            else:
                break
        if s == None:
            return 0
        s = s.split(' ')
        print(s[-1])
        return len(s[-1])

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        for i in xrange(len(s) - 1, 0, -1):
            if s[i] == ' ':
                return len(s) - i - 1
        return len(s)
a = Solution()
print(a.lengthOfLastWord("a     "))

# 58.最后一个单词的长度.py