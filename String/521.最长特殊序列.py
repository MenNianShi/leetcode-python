class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return a != b and max(len(a), len(b)) or -1
#若两字符串不相等，选择较长的字符串返回长度即可。
# 否则返回-1。（若两字符串相等，则任意字符串的子串均为另一个的子串）
# 521.最长特殊序列.py