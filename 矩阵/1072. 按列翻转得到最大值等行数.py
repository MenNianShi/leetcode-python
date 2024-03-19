#
# 方法一：哈希
# 思路与算法
#
# 题目给定 m×nm\times nm×n 的矩阵，要求从中选取任意数量的列并翻转其上的每个单元格。单元格仅包含 000 或者 111。问最多可以得到多少个由相同元素组成的行。如果某一行全部是 111 或者全部是 000，则表示该行由相同元素组成。
#
# 如果翻转固定的某些列，可以使得两个不同的行都变成由相同元素组成的行，那么我们称这两行为本质相同的行。例如 001001001 和 110110110 就是本质相同的行。
#
# 本质相同的行有什么特点呢？可以发现，本质相同的行只存在两种情况，一种是由 000 开头的行，另一种是由 111 开头的行。在开头的元素确定以后，由于翻转的列已经固定，所以可以推断出后续所有元素是 000 还是 111。
#
# 为了方便统计本质相同的行的数量，我们让由 111 开头的行全部翻转，翻转后行内元素相同的行即为本质相同的行。之后我们将每一行转成字符串形式存储到哈希表中，遍历哈希表得到最多的本质相同的行的数量即为答案。
#
#

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = {}
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if matrix[i][0] == '1':
                for j in range(m):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                    else :
                        matrix[i][j] = 0
            key = ''.join(str(matrix[i]))
            if key not in res :
                res[key] = 1
            else:
                res[key] += 1
        max_res = 0
        for k,v in res.items():
            max_res = max(max_res,v)
        return max_res

a = Solution()
print(a.maxEqualRowsAfterFlips([[0,1],[1,0]]))
# 1072. 按列翻转得到最大值等行数.py