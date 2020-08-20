# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#  
#
# 示例 1：
#
# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：
#
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#  
# 动态规划
# 此题和《最大回文子串》基本一样


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1
        dp = [[False for a in range(length)] for a in range(length)]
        dp[-1][-1] = True
        ans = 1
        for i in range(length - 1):  # 初始化长度为1和2的子串
            dp[i][i] = True
            ans += 1
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        for l in range(2, length):
            for i in range(0, length - l):
                j = i + l
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
        return ans

