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

class Solution:
    def combine(self, n, k):
        if n <= 0 or k <= 0 or k > n: return []
        nums = []
        res = []
        tmp = []
        #先在nums里生成[1,2,...,n]
        for i in range(1,n+1):
            nums.append(i)

        def backtrack(nums, tmp, k):
            if len(tmp) == k:
                res.append(tmp[:])
                return

            #剪枝：nums里剩下的个数加上tmp已经有的个数之和达不到k个，直接剪枝
            p = len(nums)
            if(p+len(tmp))<k: return
            #回溯
            for i in range(p):
                tmp.append(nums[i])
                backtrack(nums[i+1:],tmp,k)
                tmp.pop()
        backtrack(nums,[],k)
        return res


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1,n+1)]
        res = []
        def backtrack(cur,nums,start):
            if len(cur)==k and cur not in res:
                res.append(cur[:])
                return
            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(cur,nums,i+1)
                cur.pop()
        backtrack([],nums,0)
        return res