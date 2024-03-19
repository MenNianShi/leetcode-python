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
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        minLen = len(strs[0])
        for str in strs:
            if len(str) < minLen:
                minLen = len(str)

        res = ''
        for i in range(minLen):
            c = strs[0][i]
            for str in strs:
                if str[i] != c:
                    return res
            res += c

        return res
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        pre = strs[0]
        for st in strs:
            while 1:
                if st.startswith(pre):
                    break
                else:
                    pre = pre[:-1]
        return pre
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

a = Solution()
print(a.longestCommonPrefix(['']))
# 14.最长公共前缀  .py