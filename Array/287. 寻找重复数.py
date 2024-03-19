# 287. 寻找重复数
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow!= fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow