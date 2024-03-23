# 3. 无重复字符的最长子串
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        start = end = 0
        while end < len(s):
            if s[end] not in s[start:end]:
                maxLength = max(maxLength, end - start + 1)
                end += 1
            else:
                start += 1
        return maxLength