# 给你一个字符串数组words ，找出并返回length(words[i]) * length(words[j])的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回0 。
#
#
#
# 示例
# 1：
#
# 输入：words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# 输出：16
# 解释：这两个单词为
# "abcw", "xtfn"。
# 示例
# 2：
#
# 输入：words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# 输出：4
# 解释：这两个单词为
# "ab", "cd"。
# 示例
# 3：
#
# 输入：words = ["a", "aa", "aaa", "aaaa"]
# 输出：0
# 解释：不存在这样的两个单词。

#  位运算存储 信息

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bit = [0] * len(words)
        for i  in  range(len(words)):
            for ch in words[i]:
                bit[i] = bit[i] | (1 << (ord(ch) - ord('a')))
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (bit[i] & bit[j] == 0):
                    res = max(res, len(words[i]) * len(words[j]))
        return res


class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_index = s.find("01")
        max_res = 0
        while s_index != -1:
            res = 2
            i = 1
            while (s_index-i >= 0) and (s_index+i+1 < len(s)):
                if s[s_index-i] == "0" and s[s_index+i+1] == "1":
                    res += 2
                    i+=1
                else:
                    max_res = max(max_res, res)
                    break
            if (s_index + 2) <= len(s):
                tmp = s[s_index+2:]
                tmp_index = tmp.find("01")
                if tmp_index == -1:
                    max_res = max(max_res, res)
                    break
                else:
                     s_index = tmp_index + len(s[:s_index+2])
            else :
                max_res = max(max_res, res)
                break
            max_res = max(max_res,res)
        return max_res
a = Solution()
print(a.findTheLongestBalancedSubstring("01"))