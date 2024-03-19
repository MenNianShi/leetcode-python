class Solution:
    def updateBoard(self, board, click):
        i, j = click
        row, col = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白快周围的***
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < row and 0 <= j + y < col and board[i + x][j + y] == "M": res += 1
            return res

        def dfs(i, j):
            num = cal(i, j)
            if num > 0:
                board[i][j] = str(num)
                return
            board[i][j] = "B"
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    nxt_i, nxt_j = i + x, j + y
                    if 0 <= nxt_i < row and 0 <= nxt_j < col and board[nxt_i][nxt_j] == "E": dfs(nxt_i, nxt_j)

        dfs(i, j)
        return board

class Solution(object):
    m =0
    n =0
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.m = len(board)
        self.n = len(board[0])
        self.dp= [[False]*len(board[0]) for _ in range(len(board))]
        x = click[0]
        y = click[1]
        if board[x][y]=='M':
            board[x][y]='X'
            return board
        elif board[x][y]=='E':
            a = self.findE(board,x,y)
        else:
            return board
        return  board
    def findE(self,board,x,y):

        boom_cnt = 0
        if x-1>=0:
            boom_cnt += 1 if board[x-1][y]=='M' else 0
        if x+1 < self.m :
            boom_cnt += 1 if board[x+1][y]=='M' else 0
        if y-1>=0:
            boom_cnt += 1 if board[x][y-1]=='M' else 0

        if y+1 < self.n :
            boom_cnt += 1 if board[x][y+1]=='M' else 0
        if y+1 < self.n and x+1 <self.m:
            boom_cnt += 1 if board[x+1][y+1]=='M' else 0
        if y-1 >=0 and x-1 >=0:
            boom_cnt += 1 if board[x-1][y-1]=='M' else 0
        if y-1 >=0 and  x+1 <self.m:
            boom_cnt += 1 if board[x+1][y-1]=='M' else 0
        if y + 1 <self.n  and x - 1>=0:
            boom_cnt += 1 if board[x - 1][y + 1] == 'M' else 0
        if boom_cnt > 0:
            board[x][y] = str(boom_cnt)
            return

        if x-1>=0 and board[x-1][y]=='E':
            self.findE(board,x-1,y)
        if x+1<self.m and board[x+1][y]=='E':
            self.findE(board,x+1,y)
        if y-1>=0 and board[x][y-1]=='E':
            self.findE(board,x,y-1)
        if y+1<self.n and board[x][y+1]=='E':
            self.findE(board,x,y+1)
        return  board
a  = Solution()
a =  a.updateBoard([["E","E","E","E","E","E","E","E"],
                    ["E","E","E","E","E","E","E","M"],
                    ["E","E","M","E","E","E","E","E"],
                    ["M","E","E","E","E","E","E","E"],
                    ["E","E","E","E","E","E","E","E"],
                    ["E","E","E","E","E","E","E","E"],
                    ["E","E","E","E","E","E","E","E"],
                    ["E","E","M","M","E","E","E","E"]],[0,0])
for line in a:
    print(line)
    [["B", "B", "B", "B", "B", "B", "1", "E"],
     ["B", "1", "1", "1", "B", "B", "1", "M"],
     ["1", "2", "M", "1", "B", "B", "1", "1"],
     ["M", "2", "1", "1", "B", "B", "B", "B"],
     ["1", "1", "B", "B", "B", "B", "B", "B"],
     ["B", "B", "B", "B", "B", "B", "B", "B"],
     ["B", "1", "2", "2", "1", "B", "B", "B"],
     ["B", "1", "M", "M", "1", "B", "B", "B"]]
# 529. 扫雷游戏.py