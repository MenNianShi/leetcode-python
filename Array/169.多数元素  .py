def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)//2
    num_dict = {}
    for i in range(0,len(nums)):
        if nums[i] not in num_dict:
            num_dict[nums[i]] = 1
        else:
            num_dict[nums[i]]+=1
    for i in num_dict:
        if num_dict[i]>n:
            return i
print(majorityElement([1,1,1,2,3]))
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
# 169.多数元素  .py