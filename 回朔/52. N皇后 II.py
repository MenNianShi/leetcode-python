class Solution:
    def totalNQueens(self, n):
        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens,xy_diff,xy_sum):
            p=len(queens)
            if p==n:
                ans.append(queens)
                return
            #q表示新的皇后所在的列
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
        ans=[]
        DFS([],[],[])
        return len(ans)
# 52. N皇后 II.py