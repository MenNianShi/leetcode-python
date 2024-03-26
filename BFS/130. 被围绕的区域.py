# 130. 被围绕的区域
from collections import  deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        n = len(board)
        m = len(board[0])
        que = deque()
        # 标记所有边界上的 O  -> A
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
                board[i][0] = "A"
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
                board[i][m - 1] = "A"

        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
                board[0][i] = "A"
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
                board[n - 1][i] = "A"
        # 与边界相邻的点o都没被包围，所以也标记为 A
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))
                    board[mx][my] = "A"
        # 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
        # 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"