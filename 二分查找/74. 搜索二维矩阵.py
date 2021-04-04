# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m =len(matrix)
        if m <1  :
            return False
        n = len(matrix[0])
        if  n < 1:
            return False
        x = m-1
        y = 0
        while x< m and y < n and x>-1 and y >-1 :
            if target == matrix[x][y] :
                return True
            elif target>matrix[x][y] :
                y = y+1
            else:
                x = x-1
        return False
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        # binary search
        while left <= right:
            mid = (left + right) // 2
            # locate element in the matrix
            midVal = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if midVal == target: return True
            elif midVal > target: right = mid - 1
            else : left = mid + 1
        return False

