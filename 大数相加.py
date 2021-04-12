class Solution:
    def solve(self, s, t):
        # write code here
        carry = 0
        m = len(s) - 1
        n = len(t) - 1
        z = ''
        while n > -1 or m > -1 or carry != 0:
            x = 0 if m < 0 else (ord(s[m]) - ord('0'))
            y = 0 if n < 0 else (ord(t[n]) - ord('0'))
            cur = x + y + carry
            z = z + str(cur % 10)
            carry = cur // 10
            m -= 1
            n -= 1
        return z[::-1]
