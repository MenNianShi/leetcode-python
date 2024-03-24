class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        pattern = list(pattern)
        return self.helper(s,pattern) and self.helper(pattern,s)


    def helper(self,s,t):
        a = {}
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        i = 0
        while i < n:
            if s[i] not in a:
                a[s[i]] = t[i]
            else:
                if a[s[i]] != t[i]:
                    return False
            i+=1
        return True
# 290 单词规律