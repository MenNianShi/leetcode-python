# 有效数独
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True