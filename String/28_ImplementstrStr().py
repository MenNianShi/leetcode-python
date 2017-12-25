# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        if len(needle) == len(haystack):
            return 0 if needle == haystack else -1
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)