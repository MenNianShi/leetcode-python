#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
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
class Solution:


    def LIS(self, arr):
        # write code here
        if len(arr) < 2:
            return arr
        dp = [0] * len(arr)
        dp[0] = 1
        maxEnd = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] > maxEnd[-1]:
                dp[i] = len(maxEnd) + 1
                maxEnd.append(arr[i])
            else:
                idx = self.search(0, len(maxEnd), arr[i], maxEnd)
                maxEnd[idx] = arr[i]
                dp[i] = idx + 1
        length = len(maxEnd)
        ans = [0] * length
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == length:
                ans[length - 1] = arr[i]
                length -= 1
        return ans
    def search(self, left, right, num, vec):  # 在有序的vec[i, r)里二分查找num。查到返回下标；没查到返回第一个比num大的元素的下标。
        while left < right:
            mid = left + (right - left) // 2
            if vec[mid] <= num:
                left = mid + 1
            else:
                right = mid
        return left