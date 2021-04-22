# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 示例 2：
#
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        dp = [1] * n
        maxSize = 1
        maxVal = dp[0]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]
        res = []
        if maxSize == 1:
            return [nums[0]]
        for i in range(len(nums) - 1, -1, -1):
            if maxSize <= 0:
                break
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxSize -= 1
        return res
