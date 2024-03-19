class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x,y):
            if x>=len(grid) or x<0 or y<0 or y>=len(grid[0]) or grid[x][y]!=1:
                return 0
            grid[x][y]=0
            num = 1
            num += dfs(x-1,y)
            num += dfs(x+1,y)
            num += dfs(x,y+1)
            num += dfs(x,y-1)
            return num
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans,dfs(i,j))
        return ans

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                        continue
                    cur += 1
                    grid[x][y] = 0
                    for x1, y1 in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        stack.append((x + x1, y + y1))

                ans = max(ans, cur)
        return ans

# 695. 岛屿的最大面积.py