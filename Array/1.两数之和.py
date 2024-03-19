def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = []
    #nums = sorted(nums,reverse=True)
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                l.append(i)
                l.append(j)
    return l
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, n in enumerate(nums):
        	if target-n in seen:
        		return [seen[target-n], i]
        	seen[n] = i
print(twoSum([1,2,3,0],4))
print(twoSum([4,5,6,7,8,9],17))


def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hmap = {}
    for i, n in enumerate(nums):
        if n not in hmap:
            hmap[n] = (i,)
        else:
            hmap[n] = (hmap[n][0], i)#有两数相同的情况
    print(hmap)

    for n in nums:
        if target - n in hmap:
            if target - n == n and len(hmap[target - n]) == 1:
                continue
            return hmap[n][0], hmap[target - n][-1] #此处-1使去两数相同情况的后一个数
print(twoSum([4,5,6,7,8,9,9],17))
# 1.两数之和.py