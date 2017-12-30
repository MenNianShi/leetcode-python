# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6
class Solution(object):
    def computeArea(self, grid, x, y):
        grid[x][y] = 0
        area = 1

        if x > 0 and grid[x - 1][y] == 1:
            area += self.computeArea(grid, x - 1, y)

        if x < self.numRows - 1 and grid[x + 1][y] == 1:
            area += self.computeArea(grid, x + 1, y)

        if y > 0 and grid[x][y - 1] == 1:
            area += self.computeArea(grid, x, y - 1)

        if y < self.numCols - 1 and grid[x][y + 1] == 1:
            area += self.computeArea(grid, x, y + 1)

        return area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.numRows = len(grid)
        self.numCols = len(grid[0])
        maxArea = 0

        for i in xrange(self.numRows):
            for j in xrange(self.numCols):
                if grid[i][j] == 1:
                    area = self.computeArea(grid, i, j)
                    if area > maxArea:
                        maxArea = area

        return maxArea