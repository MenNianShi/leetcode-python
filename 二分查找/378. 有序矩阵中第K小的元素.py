# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
#
#  
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row =len(matrix)
        col = len(matrix[0])
        left = matrix[0][0]
        right = matrix[row-1][col-1]
        while left < right:
            mid = left+(right-left)//2
            cnt = self.findcnt(matrix,mid,row,col)
            if cnt < k:
                left = mid+1
            else:
                right = mid
        return right

    def findcnt(self,matrix,mid,row,col):
        i = row - 1
        j = 0
        count = 0
        while (i >= 0 and j < col) :
            if (matrix[i][j] <= mid) :
                 #第j列有i+1个元素 <= mid
                count += i + 1
                j=j+1
            else :
                # 第j列目前的数大于mid，需要继续在当前列往上找
                i-=1
        return count

# 378. 有序矩阵中第K小的元素.py