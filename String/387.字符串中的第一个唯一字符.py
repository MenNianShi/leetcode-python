import math
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    str_dict = {}
    a=''
    for i in s:
        if i not in str_dict:
            str_dict[i] = 1
        else:
            str_dict[i]+=1
    for i,k in enumerate(str_dict):
        if str_dict[k]==1:
            a=k
            break
    for j,key in enumerate(s):
        if key==a:
            return j
    return -1
print(firstUniqChar("leetcode"))
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for i in xrange(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        # index=[s.index(l) for l in letters if s.count(l) == 1]
        # return min(index) if len(index) > 0 else -1
        index = [s.index(l) for l in letters if s.count(l) == 1]
        if len(index) > 0:
            return min(index)
        else:
            return -1
# 387.字符串中的第一个唯一字符.py