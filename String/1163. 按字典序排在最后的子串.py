# 给你一个字符串
# s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
#
#
#
# 示例
# 1：
#
# 输入：s = "abab"
# 输出："bab"
# 解释：我们可以找出
# 7
# 个子串["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是
# "bab"。
# 示例
# 2：
#
# 输入：s = "leetcode"
# 输出："tcode"
# 双指针
# 记字符串 s 的长度为 n。首先并非所有的子字符串都需要被考虑到，只有后缀子字符串才可能是排在最后的子字符串。
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]


# 1163. 按字典序排在最后的子串.py