# Write a function to find the longest common prefix string amongst an array of strings.
from numpy.core.tests.test_mem_overlap import xrange
class Solution:
    def longestCommonPrefix(self, strs):
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort(key=lambda x:len(x))
        n = len(strs[0])
        res = ''
        i = 0
        while i < n:
            cur_c = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != cur_c:
                    return res
            res += cur_c
            i+=1
        return res
# 14.最长公共前缀  .py