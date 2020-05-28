# 给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
#
# 请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
#
# 每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
#
# 题目保证一定有解。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。

class Solution:
    def smallestDivisor(self, nums,threshold ):
        l, r, ans = 1, max(nums) + 1, -1
        while l <= r:
            mid = (l + r) // 2
            total = sum((x - 1) // mid + 1 for x in nums)
            if total <= threshold:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left<=right:
            mid = left + (right-left)//2
            if self.candiv(nums,mid,threshold):
                right = mid-1
            else:
                left = mid+1
        return left
    def candiv(self, nums: List[int], target:int,threshold: int) -> bool:
        summ = 0
        for num in nums:
            summ += math.ceil(num/target)
        if summ <=threshold:
            return True
        else:
            return False
a = Solution()
print(a.smallestDivisor([1,2,5,9],6))