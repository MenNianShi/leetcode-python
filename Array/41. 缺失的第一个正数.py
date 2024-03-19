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

class Solution:
    def firstMissingPositive(self, nums) :
        dict={i:i for i in nums if i>0}
        n=len(dict)
        for i in range(1,n+1):
            if i not in dict:
                return i
        return n+1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = {}
        for num in nums:
            num_set[num] = 0
        i = 1
        while i not in num_set:
            i += 1
        return i
a = Solution()
print(a.firstMissingPositive([1,2,0]))

# 41. 缺失的第一个正数.py