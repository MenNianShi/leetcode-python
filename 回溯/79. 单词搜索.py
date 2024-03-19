# 79. 单词搜索

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if (newi, newj) not in visited:
                        if backtrack(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        visited = set()
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False