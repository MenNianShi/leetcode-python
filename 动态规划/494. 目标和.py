# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        all_sum = sum(nums)
        diff = all_sum - target
        if diff<0 or diff%2!=0:
            return 0
        n = len(nums)
        neg  = diff/2
        dp = [[0]*(neg+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(0,neg+1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]





#回溯
class Solution(object):
    count = 0

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def backtrack(nums, target, index, sum):
            if index == len(nums):
                if sum == target:
                    self.count += 1
            else:
                backtrack(nums, target, index + 1, sum + nums[index])
                backtrack(nums, target, index + 1, sum - nums[index])

        backtrack(nums, target, 0, 0)
        return self.count


# 494. 目标和.py