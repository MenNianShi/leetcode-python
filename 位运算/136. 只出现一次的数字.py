# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#

class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

# 136. 只出现一次的数字.py