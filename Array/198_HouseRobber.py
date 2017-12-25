from numpy.core.tests.test_mem_overlap import xrange


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxpro = 0
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums)
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]>maxpro:
                maxpro = nums[i]+nums[j]
    return maxpro
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums)==0:
        #    return 0
        best=[0,0]
        #best.append(nums[0])
        for i in range(len(nums)):
            best.append(max(nums[i]+best[-2],best[-1]))
        return best[-1]
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robbest = [0] * (len(nums) + 2)
        for i in xrange(2, len(nums) + 2):
            robbest[i] = max(robbest[i - 1], nums[i - 2] + robbest[i - 2])
        return robbest[-1]
a = Solution()
print(a.rob([3,2,6,4,5]))