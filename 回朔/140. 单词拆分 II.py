# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

class Solution:#超时
    def wordBreak(self, s, wordDict):
        ans = []
        n = len(s)

        def backtrack(temp, start):
            if start == n: ans.append(temp[1:])
            for i in range(start, n):
                if s[start:i + 1] in wordDict:
                    backtrack(temp + " " + s[start:i + 1], i + 1)
        backtrack('', 0)
        return ans


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    # print stringlist+' '+s[:i]
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])

    def check(self, s, wordDict):
            dp = [False for i in range(len(s)+1)]
            dp[0] = True
            for i in range(len(s)):
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i + 1] in wordDict:
                        dp[i + 1] = True
                        break
            return dp[len(s)]

