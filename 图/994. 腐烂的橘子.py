class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 检查是否有独立的 新鲜橘子
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        def neighbor(i, j):
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        d = 0
        while queue:
            i, j, d = queue.popleft()
            for x, y in neighbor(i, j):
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y, d + 1))
        if any(1 in row for row in grid):
            return -1
        return d


# 994 腐烂的橘子