

class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        def isVowelString(word):
            return isVowelLetter(word[0]) and isVowelLetter(word[-1])
        def isVowelLetter(c):
            return c in ('a','e','i','o', 'u')
        n = len(words)
        prefix_sums = [0] * (n+1)
        for i in range(n):
            value = 1 if isVowelString(words[i]) else 0
            prefix_sums[i+1] = prefix_sums[i] + value
        ans = []
        for i in range(len(queries)):
            start, end = queries[i]
            ans.append(prefix_sums[end+1]-prefix_sums[start])
        return ans



# 2559. 统计范围内的元音字符串数.py