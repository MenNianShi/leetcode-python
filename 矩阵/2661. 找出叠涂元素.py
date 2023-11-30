# 维护两个数组 存储 行列 已涂个数，涂满返回即可
class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        m = len(mat[0])
        mp = {}
        for i in range(n):
            for j in range(m):
                mp[mat[i][j]] = [i, j]
        rowCnt, colCnt = [0] * n, [0] * m
        for i in range(len(arr)):
            v = mp[arr[i]]
            rowCnt[v[0]] += 1
            if rowCnt[v[0]] == m:
                return i
            colCnt[v[1]] += 1
            if colCnt[v[1]] == n:
                return i
        return -1



