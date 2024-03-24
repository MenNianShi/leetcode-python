import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = collections.defaultdict(int)
        if len(s)!=len(t):
            return False
        for c in t:
            m[c] +=1
        for c in s:
            if c not in m :
                return False
            else:
                m[c]-=1
                if m[c] == 0:
                    del m[c]
        return True
# 242.有效的字母异位词