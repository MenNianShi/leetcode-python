# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(cur,nums):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtrack(cur,nums[:])
                cur.pop()
        backtrack([],nums)
        return res
a = Solution()
print(a.permute([1,2,3]))
# 46. 全排列.py