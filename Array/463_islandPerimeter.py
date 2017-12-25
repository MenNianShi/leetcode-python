
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    i=0
    j=0
    islandLength=0
    while i<len(grid):
        j=0
        while j<len(grid[0]):
            if grid[i][j]==1:
                islandLength = islandLength+4
                if (i > 0 and grid[i - 1][j] == 1):
                    islandLength = islandLength-1
                if (j > 0 and grid[i][j - 1] == 1):
                    islandLength = islandLength - 1
                if (i < len(grid)-1 and grid[i + 1][j] == 1):
                    islandLength = islandLength - 1
                if (j < len(grid[0])-1 and grid[i][j + 1] == 1):
                    islandLength = islandLength - 1
            j=j+1
        i= i+1
    return islandLength
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(len(grid))

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))


def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] == 1:
                res += 4
                # Check Neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    res -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    res -= 2
    return res

