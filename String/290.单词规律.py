# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        word_dict = {}
        if len(pattern)!= len(s):
            return False
        for i in range(0,len(pattern)):
            if pattern[i] not in word_dict:
                word_dict[pattern[i]] = s[i]
            else:
                if s[i]!= word_dict[pattern[i]]:
                    return False
        for k in word_dict.keys():
            for j in word_dict.keys():
                if word_dict[k]==word_dict[j]:
                    if k!=j:
                        return False

        return True
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        dic = {}
        for i in xrange(len(words)):
            if pattern[i] in dic:
                if words[i] != dic[pattern[i]]:
                    return False
            elif words[i] in dic.values():
                return False
            dic[pattern[i]] = words[i]
        return True
a = Solution()
print(a.wordPattern("jquery","jquery"))

# 290.单词规律.py