# 55. 跳跃游戏
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = nums[0]
        i = 0
        while i < len(nums) and i <= reach:
            reach = max(reach,nums[i] + i)
            i+=1
        if reach >= len(nums)-1:
            return True
        else:
            return False