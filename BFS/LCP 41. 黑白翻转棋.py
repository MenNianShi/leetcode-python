# 可以用「广度优先搜索」来解决这个问题，我们对每一个空余位置尝试黑棋放置，
# 用一个队列来存储正在进行「翻转操作」的黑棋位置，若队列非空，我们从队列中取出队首元素，
# 进行行、列和对角线 888 个方向判断是否有可以翻转的白棋——判断沿着方向是否是连续的一段白棋并以另一颗黑棋结尾。
# 若有可以翻转的白棋，则将这些白旗进行翻转，并加入队列中。直至队列为空表示一次放置黑棋结束。
#
# 初始可以放置黑棋的全部位置中可以翻转的白棋个数最大值即为最后的答案。
class Solution(object):
    def flipChess(self, chessboard):
        """
        :type chessboard: List[str]
        :rtype: int
        """
        def judge(chessboard,x,y,dx,dy):
            x+=dx
            y+=dy
            while 0 <= x < len(chessboard) and 0 <= y < len(chessboard[0]):
                if chessboard[x][y] == "X":
                    return True
                elif chessboard[x][y] == ".":
                    return False
                x += dx
                y += dy
            return False
        def bfs(chessboard,px,py):
            chessboard = [list(row) for row in chessboard]
            cnt = 0
            q = deque([(px,py)])
            chessboard[px][py] = "X"
            while q:
                tx,ty = q.popleft()
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx == dy ==0 :
                            continue
                        if judge(chessboard,tx,ty,dx,dy):
                            x,y = tx+dx,ty +dy
                            while chessboard[x][y] != "X":
                                q.append((x,y))
                                chessboard[x][y] = "X"
                                x += dx
                                y += dy
                                cnt+=1
            return cnt
        res = 0
        for i in range(len(chessboard)):
            for j in range(len(chessboard[0])):
                if chessboard[i][j] == '.':
                    res = max(res,bfs(chessboard,i,j))
        return res