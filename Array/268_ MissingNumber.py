#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#0到n（包括n，n为数组长度）中少了一个数，找出这个数
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = set(nums)
    for i in range(0, len(nums) + 1):
        if i not in a:
            return i
print(missingNumber([0]))