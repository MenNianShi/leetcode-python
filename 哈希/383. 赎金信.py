# 383. 赎金信
import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = collections.defaultdict(int)

        for c in magazine:
            m[c] +=1
        for c in ransomNote:
            if c not in m :
                return False
            else:
                m[c]-=1
                if m[c] == 0:
                    del m[c]
        return True