class Solution(object):
    def helper(self, n, s):
        if not n:
            return s
        pre = s[0]
        res = ''
        count = 1
        for i in range(1, len(s)):
            if s[i] == pre:
                count += 1
            else:
                res += str(count) + pre
                count = 1
                pre = s[i]
        res += str(count) + pre
        return self.helper(n - 1, res)

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1:
            return s
        return self.helper(n - 1, s)



