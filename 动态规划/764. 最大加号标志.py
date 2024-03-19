# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0
#
# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
#
# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。
#

class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        dp = [[n] * n for _ in range(n)]
        print(dp)
        banned = set(map(tuple, mines))
        print(banned)
        for i in range(n):
            # left
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # right
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            # up
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # down
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        return max(map(max, dp))

a= Solution()
a.orderOfLargestPlusSign(5,[[1,1]])

class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mat = [[1] * n for _ in range(n)]
        for item in mines:
            mat[item[0]][item[1]] = 0
        res = 0
        for i in range(n):
            for j in range(n):
                up = 0
                down = 0
                left = 0
                right = 0
                cur = min(i+1,j+1,n-i,n-j)
                if cur < res :
                    continue
                while i-up >= 0 and  mat[i-up][j] ==1 and mat[i][j]==1:
                    up = up+1
                while i+down < n and  mat[i+down][j] ==1 and mat[i][j]==1:
                    down = down+1
                while j+right < n and  mat[i][j+right] ==1 and mat[i][j]==1:
                    right = right+1
                while j-left >= 0 and  mat[i][j-left] ==1 and mat[i][j]==1:
                    left = left+1
                cur_max_k = min(up,down,left,right)
                res = max(cur_max_k,res)
        return res
# 764. 最大加号标志.py