class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = self.turn(matrix)
        return res

    def turn(self, arr):
        row = len(arr)
        col = len(arr[0])
        B = []
        for j in range(col):
            A = []
            for i in range(row):
                A.append(arr[i][j])

            B.append(A)
        B.reverse()
        return B