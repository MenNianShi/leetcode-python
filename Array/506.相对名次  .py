def findRelativeRanks(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    rank_dict={}
    for i,k in enumerate(sorted(nums,reverse=True)):
        rank_dict[k]=i+1
    for i in range(0,len(nums)):
        if rank_dict[nums[i]] == 1:
            nums[i] = 'Gold Medal'
        elif rank_dict[nums[i]] == 2:
            nums[i] = 'Silver Medal'
        elif rank_dict[nums[i]] == 3:
            nums[i] = 'Bronze Medal'
        else:
            nums[i] = str(rank_dict[nums[i]])
    return nums

print(findRelativeRanks([10,3,8,9,4]))