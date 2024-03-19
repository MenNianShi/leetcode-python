class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # row, col = len(matrix), len(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
import  numpy as np
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        matrix = np.array(matrix)
        return self.helper(matrix)
    def helper(self,matrix, flag=None):
        m = len(matrix)
        if m == 0:
            return True
        n = len(matrix[0])
        if n == 0:
            return True
        x = min(m,n)
        start = matrix[0][0]
        for i in range(x):
            if i!=0:
                if matrix[i][i]!=start:
                    return False
        if flag == 'left':
            return self.helper(matrix[1:,:],'left')
        if flag == 'right':
            return self.helper(matrix[:,1:],'right')
        left = self.helper(matrix[1:,:],'left')
        right = self.helper(matrix[:,1:],'right')
        return  left and right
A = Solution()
a = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
b = [[11,74,0,93],[40,11,74,7]]

print(A.isToeplitzMatrix(a))



# 766. 托普利茨矩阵.py