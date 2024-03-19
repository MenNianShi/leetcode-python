# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
# Example 1:
#
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0

        lastC = 0
        curC = 1
        cur = s[0]

        result = 0
        for i in s[1:]:
            if i != cur:
                cur = i
                lastC = curC
                curC = 1
                result += 1
            else:
                if lastC > curC:
                    result += 1
                curC += 1

        return result
# 696.计数二进制子串  .py