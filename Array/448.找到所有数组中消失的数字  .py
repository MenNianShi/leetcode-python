def findDisappearedNumbers(nums):#超时
    """
    :type nums: List[int]
    :rtype: List[int]
    """


    if nums==[]:
        return nums
    else:
        initlength = len(nums)
        for i in range(0,initlength):
            if (i+1) not in nums:
                nums.append(i+1)
        return nums[initlength:]


print(findDisappearedNumbers([1,1]))


def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    ret = set(range(1, len(nums) + 1))
    ret = ret - set(nums)
    return list(ret)
def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    l = len(nums)+1
    nums = set(nums)
    return [i for i in range(1, l) if i not in nums]
# 448.找到所有数组中消失的数字  .py