# 131. 分割回文串
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        def isPalindrome(i,j):
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1
        def backtrack(cur,index):
            if index == len(s):
                res.append(cur[:])
            for j in range(index,n):
                if isPalindrome(index,j) ==1:
                    cur.append(s[index:j+1])
                    backtrack(cur,j+1)
                    cur.pop()
        backtrack([],0)
        return res

