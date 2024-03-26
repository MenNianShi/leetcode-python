# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(cur,index):
            if len(cur) == k and cur not in res:
                res.append(cur[:])
                return
            for i in range(index,n+1):
                cur.append(i)
                backtrack(cur,i+1)
                cur.pop()
        backtrack([],1)
        return res
# 77. 组合.py