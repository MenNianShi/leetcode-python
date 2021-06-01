class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        hash_dict = {0:-1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = cur_sum+nums[i]
            reminder = cur_sum % k
            if reminder in hash_dict:
                pre_index = hash_dict[reminder]
                if i - pre_index >= 2:
                    return True
            else:
                hash_dict[reminder] = i
        return False

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        hash_dict = {0:-1}
        reminder = 0
        for i in range(len(nums)):
            reminder = (reminder+nums[i]) % k
            if reminder in hash_dict:
                pre_index = hash_dict[reminder]
                if i - pre_index >= 2:
                    return True
            else:
                hash_dict[reminder] = i
        return False
