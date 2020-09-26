# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#

class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(nums,start,tempPath):
            res.append(tempPath[:])
            for i in range(start,len(nums)):
                tempPath.append(nums[i])
                backtrack(nums,i+1,tempPath)
                tempPath.pop()
        backtrack(nums,0,[])
        return res


result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

