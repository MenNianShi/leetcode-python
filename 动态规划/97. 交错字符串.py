# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
#
# 示例 1:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 示例 2:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
#
# 动态规划
# 用二维数组dp记录通过交叉s1前i个字符，和s2前j个字符，能否得到s3前（i+j）个字符。
# 考虑到s3[i+j]的字符要么来自s1[i]，要么来自s2[j] （或运算）。于是可以想到状态方程应是
# dp[i][j] = (dp[i-1][j] and (s3[i+j-1] == s1[i-1])) or (dp[i][j-1] and (s3[i+j-1] == s2[j-1]))
# 上式 or 的左边是最后一个字符来自s1[i]的情况，or的右边是最后一个字符来自s2[j]的情况。
#
# 初始化dp数组时，设置dp为len(s1)+1行，len(s2)+1列，值全部为False。
# 为了满足使用上述状态方程，需要先初始化第一行和第一列。dp数组的第一行和第一列表示是否能只用s1或者s2的前x个字符，组成s3的前x个字符。注意设置dp[0][0] = True。
# 最后输出最后面的布尔值即可。

class Solution:
    def isInterleave(self, s1, s2, s3):
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]

