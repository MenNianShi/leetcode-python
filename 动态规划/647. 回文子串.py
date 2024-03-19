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

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cnt= 0
        for k in range(n):
            for i in range(n-k):
                j = i+k
                print(i,j)
                if k==0 :  # 长度为1 的情况
                    dp[i][j] = True
                elif k==1: # 长度为2 的情况
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j]: cnt+=1
        return cnt
a= Solution()
print(a.countSubstrings('aaa'))

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(i,n):
                print(i,j)
                if i==j:
                    dp[i][j] = True
                elif j-i==1:
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] : cnt+=1
        return cnt
a = Solution()
print(a.countSubstrings('aaa'))
# 647. 回文子串.py