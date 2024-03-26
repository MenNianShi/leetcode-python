# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#  
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n_dict = {}
        for i in range(n):
            if nums[i] > 0:
                n_dict[nums[i]] = nums[i]
        for i in range(1,n+1):
            if i not in n_dict:
                return i
        return n+1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n): # 最大返回n+1，负数都置为n+1
            if nums[i] <=0 :
                nums[i] = n+1
        for i in range(n):
            num = abs(nums[i])
            if num <= n :# 由于非负数都是n+1了，所以此处均为非负数，非负数，在[1,n] 符合要求的数，都是负数了
                nums[num-1] = -abs(nums[num-1])
        for i in range(n):
            if nums[i] > 0: # 大于 0 的都是
                return i+1
        return n + 1
a = Solution()
print(a.firstMissingPositive([1,2,0]))

# 41. 缺失的第一个正数.py