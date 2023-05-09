# 给出一个单词数组words ，其中每个单词都由小写英文字母组成。
#
# 如果我们可以不改变其他字符的顺序 ，在wordA 的任何地方添加恰好一个 字母使其变成wordB ，那么我们认为wordA是wordB的 前身 。
#
# 例如，"abc"是"abac"前身 ，而"cba"不是bcad"的前身词链是单词[word_1, word_2, ..., word_k]组成的序列，k >= 1，其中
# word1是word2的前身，word2是word3的前身，依此类推。一个单词通常是k == 1的单词链 。 从给定单词列表words中选择单词组成词链，返回词链的最长可能长度 。
#
# 示例
# 1： 输入：words = ["a", "b", "ba", "bca", "bda", "bdca"]
# 输出：4
# 解释：最长单词链之一为["a", "ba", "bda", "bdca"]
# 示例
# 2:
# 输入：words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
# 输出：5
# 解释：所有的单词都可以放入单词链["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# 示例
# 3:
# 输入：words = ["abcd", "dbqca"]
# 输出：1
# 解释：字链["abcd"]
# 是最长的字链之一。["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        cnt = {}
        words.sort(key=len)
        for word in words:
            cnt[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in cnt:
                    cnt[word] = max(cnt[word], cnt[prev] + 1)
            res = max(res, cnt[word])
        return res

