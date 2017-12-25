def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = 0
    for i in range(0,):
        if i==0:
            nums
            count=count+1
    for i in range(0,count):
        nums.append(0)
    print(nums)
moveZeroes([0,0,1])


def moveZeroes( nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    #j始终指向第一个0，把所有元素都与第一个0交换位置
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
moveZeroes([1,0,3,0,1,12])


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in xrange(i, len(nums)):
            nums[j] = 0

