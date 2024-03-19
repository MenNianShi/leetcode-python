class Solution: #DFS + backtraveling
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def check(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        for row in range(9):
            if board[row][y] == tmp:
                return False
        for col in range(9):
            if board[x][col] == tmp:
                return False
        for row in range(3):
            for col in range(3):
                if board[(x / 3) * 3 + row][(y / 3) * 3 + col] == tmp:
                    return False
        board[x][y] = tmp
        return True
    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row, col, board) and self.dfs(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True
    def solveSudoku(self, board):
        self.dfs(board)
# 37. 解数独.py