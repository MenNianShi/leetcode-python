# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
#
# 示例：
#
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]

class Solution(object):
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(land), len(land[0])
        def dfs(x,y) :
            if x< 0 or x>=m or y< 0 or y>= n or land[x][y]!=0:
                return 0
            land[x][y] = -1
            res = 1
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx ==0 and dy ==0:
                        continue
                    res += dfs(x+dx,y+dy)
            return res
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(dfs(i,j))
        res.sort()
        return res
# 面试题 16.19. 水域大小.py