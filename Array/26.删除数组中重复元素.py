def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    print(nums)
    return len(nums)
def removeDuplicates( nums):
    if len(nums)==0:
        return 0
    j=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[j]:
            nums[j+1]=nums[i]
            j=j+1
    print(nums)
    return  j+1
nums = [1,1,2]
print(removeDuplicates(nums))