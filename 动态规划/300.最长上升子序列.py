# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
        #dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。  所以这里 用 max(dp) 而非 dp[-1]
        return max(dp)
a = Solution()
print(a.lengthOfLIS([1,3,6,7,9,4,10,5,6]))