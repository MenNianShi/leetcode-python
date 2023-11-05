# DNA序列 由一系列核苷酸组成，缩写为
# 'A', 'C', 'G'和'T'.。
#
# 例如，"ACGAATTCCG"是一个DNA序列 。在研究DNA时，识别DNA中的重复序列非常有用。
#
# 给定一个表示DNA序列的字符串s ，返回所有在分子中出现不止一次的长度为10(子字符串)。你可以按任意顺序返回答案。
# 示例
# 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
# 示例
# 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        cnt = {}
        for i in range(len(s)- 10 + 1):
            sub = s[i :i + 10]
            if sub not in cnt:
                cnt[sub] = 1
            else:
                cnt[sub] +=1
            if cnt[sub] == 2:
                res.append(sub)
        return res
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) <= 10:
            return res
        for i in range(0,len(s)-10):
            cur_s = s[i:i+10]
            if  cur_s in s[i+1:]:
                if cur_s not in res :
                    res.append(cur_s)
        return res