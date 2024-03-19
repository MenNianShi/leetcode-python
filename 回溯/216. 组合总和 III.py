# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candiates=[1,2,3,4,5,6,7,8,9]
        def dfs(sublist,n,cur_num,begin):
            if k==cur_num and n==0:
                res.append(sublist[:])
            for i in range(begin,len(candiates)):
                if candiates[i] not in sublist:
                    sublist.append(candiates[i])
                    dfs(sublist,n-candiates[i],cur_num+1,i+1)
                    sublist.pop()
        dfs([],n,0,0)
        return res

# 216. 组合总和 III.py