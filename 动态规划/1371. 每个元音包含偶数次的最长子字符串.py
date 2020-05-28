class Solution:
    i_mapper = {
        "a": 0,
        "e": 1,
        "i": 2,
        "o": 3,
        "u": 4
    }
    def check(self, s, pre, l, r):
        for i in range(5):
            if s[l] in self.i_mapper and i == self.i_mapper[s[l]]: cnt = 1
            else: cnt = 0
            if (pre[r][i] - pre[l][i] + cnt) % 2 != 0: return False
        return True
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)

        pre = [[0] * 5 for _ in range(n)]

        # pre
        for i in range(n):
            for j in range(5):
                if s[i] in self.i_mapper and self.i_mapper[s[i]] == j:
                    pre[i][j] = pre[i - 1][j] + 1
                else:
                    pre[i][j] = pre[i - 1][j]
        for i in range(n - 1, -1, -1):
            for j in range(n - i):
                if self.check(s, pre, j, i + j):
                    return i + 1
        return 0
