class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def help(s, k, mi, ma):
            st = set()
            t = 0
            for r in range(len(s)):
                t = t * 2 + (int)(s[r])
                if r >= k:
                    t -= int(s[r - k]) << k
                if r >= k - 1 and t >= mi and t <= ma:
                    st.add(t)
            return len(st) == ma - mi + 1
        if n == 1:
            return s.find('1') != -1
        k = 30
        while (1 << k) >= n:
            k -= 1
        if len(s) < (1 << (k - 1)) + k - 1 or len(s) < n - (1 << k) + k + 1:
            return False
        return help(s, k, 1 << (k - 1), (1 << k) - 1) and help(s, k + 1, 1 << k, n)
# 1016. 子串能表示从 1 到 N 数字的二进制串.py