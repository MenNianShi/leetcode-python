class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x,y):
            grid[x][y]=0
            for x1,y1 in [(1,0),(0,1),(-1,0),(0,-1)]:
                cur_x = x+x1
                cur_y = y+y1
                if cur_x>=0 and cur_y>=0 and cur_x<len(grid) and cur_y <len(grid[0]) and grid[cur_x][cur_y]=='1':
                    dfs(cur_x,cur_y)
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num+=1
                    dfs(i,j)
        return num