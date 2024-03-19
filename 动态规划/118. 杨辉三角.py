# 118. 杨辉三角
class Solution:
    def generate(self, numRows):
        res = [[1], [1, 1]]
        if numRows <= 2:
            return res[:numRows]
        else:
            for i in range(2,numRows):
                cur_row = [1]
                for j in range(i-1):
                    cur_row.append(res[i - 1][j] + res[i- 1][j +1])
                cur_row.append(1)
                res.append(cur_row)
            return res