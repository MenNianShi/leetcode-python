# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        visited = [False] * len(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for i in range(0, len(nums)):
                if (visited[i]) or (i > 0 and visited[i - 1] == True and nums[i] == nums[i - 1]):
                    continue
                visited[i] = True
                backtrack(cur + [nums[i]])
                visited[i] = False

        backtrack([])
        return res
