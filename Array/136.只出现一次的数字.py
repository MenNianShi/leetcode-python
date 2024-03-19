def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    i=0
    while(i<len(nums)):
        if i+1<len(nums) and nums[i]==nums[i+1]:
            i=i+2
        else:
            return nums[i]

    return nums[-1]



print(singleNumber([1,2,3,2,4,5,4,5,1]))

#交换律a ^ b = b ^ a，性质2：0 ^ a = a。于是利用交换律可以将数组假想成相同元素全部相邻，于是将所有元素依次做异或操作，
# 相同元素异或为0，最终剩下的元素就为Single Number。时间复杂度O(n)，空间复杂度O(1)
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0
    for num in nums:
        n = n ^ num
    return n
# 136.只出现一次的数字.py