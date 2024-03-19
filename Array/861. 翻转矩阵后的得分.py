# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
#
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
#
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
#
# 返回尽可能高的分数。
#
#  
#
# 示例：
#
# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        #第一列 的 0 的行， 对行 进行反转
        for i in range(m):
            if A[i][0] == 0:
                for j in range(0,n):
                    A[i][j] = 1-A[i][j]
        # 后面的列 0的个数多的， 对列进行反转
        for j in range(1,n):
            zero_cnt = 0
            for i in range(m):
                if A[i][j] == 0:
                    zero_cnt+=1
            if zero_cnt > m - zero_cnt:
                for i in range(m):
                    A[i][j] = 1-A[i][j]
        res = 0
        for i in range(m):
            for j in range(n-1,-1,-1):
                res += A[i][j] * int(pow(2, n - 1 - j))
        return res
A  = Solution()
print(A.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
# 861. 翻转矩阵后的得分.py