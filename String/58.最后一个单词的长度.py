class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        start = -1
        end = n - 1
        while s[end] == ' ':
            end -= 1
        for i in range(end, -1, -1):
            if s[i] == ' ':
                start = i
                break
        return end - start

# 58.最后一个单词的长度.py