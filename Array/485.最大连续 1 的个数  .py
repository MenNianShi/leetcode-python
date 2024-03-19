def findMaxConsecutiveOnes( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxlength = 0
    count = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count = 1
            j = i
            while ((j + 1) < len(nums) and nums[j + 1] != 0):
                count = count + 1
                j = j + 1
            if count > maxlength:
                maxlength = count
    return maxlength
def findMaxConsecutiveOnes( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxlength = 0
    length =0
    for i in range(0,len(nums)):
        if nums[i]==0:
            length = 0
        else:
            length = length+1
        if length>maxlength:
            maxlength = length

    return maxlength
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
# 485.最大连续 1 的个数  .py