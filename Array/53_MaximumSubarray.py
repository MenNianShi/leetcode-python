# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
def maxSubArray(nums):#超时
    """
    :type nums: List[int]
    :rtype: int
    """
    maxSum= max(nums)

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            k = sum(nums[i:j])
            if sum(nums[i:j+1])>maxSum:
                maxSum = sum(nums[i:j+1])
    return maxSum
#用max_sum表示最终结果，this_sum表示目前最大的和。基本思想是，一旦子串小于0，就从新的位置开始求和（因为加上一个负数只会更小）
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = nums[0]
        this_sum = 0
        for num in nums:
            this_sum += num
            if this_sum > max_sum:
                max_sum = this_sum
            if this_sum <= 0:
                this_sum = 0
        return max_sum
print(maxSubArray([-1,-1,-1,-1,-1]))
a = Solution()
print(a.maxSubArray([-1,0,-1,-1,-1]))