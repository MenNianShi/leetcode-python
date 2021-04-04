# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pre_sum = {}
        pre_sum[0]=1
        sum_0 = 0
        ans = 0
        for i in range(n):
            sum_0+=nums[i]
            sum_j =(sum_0-k)
            if sum_j in pre_sum:
                ans+=pre_sum[sum_j]
            if sum_0 in pre_sum:
                pre_sum[sum_0]+=1
            else:
                pre_sum[sum_0]=1
        return ans
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        preSum = 0
        res = 0
        for  num in nums:
            preSum +=num
            if (preSum-k) in d:
                res+=d[preSum-k]
            if preSum not in d:
                d[preSum]=1
            else:
                d[preSum]+=1
        return res
a=  Solution()
print(a.subarraySum([1,1,1],2))