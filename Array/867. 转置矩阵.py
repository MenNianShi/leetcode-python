# 尺寸为 R x C 的矩阵 A 转置后会得到尺寸为 C x R 的矩阵 ans，对此有 ans[c][r] = A[r][c]。
#
# 让我们初始化一个新的矩阵 ans 来表示答案。然后，我们将酌情复制矩阵的每个条目。

class Solution(object):
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
# 867. 转置矩阵.py