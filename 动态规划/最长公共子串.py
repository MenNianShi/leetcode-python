def find_lcsubstr(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列 s1[:i] 和 s[:j] 的最长公共前缀
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            if dp[i + 1][j + 1] > mmax:
                mmax = dp[i + 1][j + 1]
                p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度

# 最长公共子串.py