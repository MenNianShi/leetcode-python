class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        if n==0 or n==1:
            return n
        dp = [[0]*n for _ in range(n)]
        max_len = 0
        for i in range(n):
            dp[i][i] = True
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if (i-j)==1:
                    dp[j][i] = A[i]==A[j]
                    max_len = max(max_len,i-j+1)
                else:
                    if dp[j+1][i-1] and A[i]==A[j]:
                        dp[j][i]=True
                        max_len = max(max_len,i-j+1)
                    else:
                        dp[j][i] = False
        return max_len
# 最长回文子串的长度.py