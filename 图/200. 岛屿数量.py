class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res  = 0
        def dfs(i,j):
            grid[i][j]=0
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                cur_x = i + x
                cur_y = j + y
                if cur_x>=0 and cur_y>=0 and cur_x<len(grid) and cur_y <len(grid[0]) and grid[cur_x][cur_y]=='1':
                    dfs(cur_x,cur_y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        return res
# 200. 岛屿数量.py