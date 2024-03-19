def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = []

    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
# 35.搜索插入位置  .py