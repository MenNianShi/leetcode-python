# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        res = []
        visit = set()  # 去重

        def dfs(index, arr):
            if len(arr) > 1 and tuple(arr) not in visit:  # arr长度大于1，且未出现
                res.append(arr[:])
                visit.add(tuple(arr))
            for i in range(index + 1, n):
                if nums[i] >= arr[-1]:  # 大于等于最后的值，说明添加上该值满足自增条件
                    arr.append(nums[i])
                    dfs(i, arr)
                    arr.pop()  # 回溯

        for i in range(n):  # 从每一个下标作为起点，递归
            dfs(i, [nums[i]])
        return res
