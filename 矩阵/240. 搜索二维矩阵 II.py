class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m  = len(matrix)
        n = len(matrix[0])
        x = m-1
        y = 0
        while x<m and y<n and x>-1 and y>-1:
            if target == matrix[x][y]:
                return True
            elif target> matrix[x][y]:
                y = y+1
            else:
                x = x-1
        return False
