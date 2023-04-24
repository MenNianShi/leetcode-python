# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(0,len(nums)):
            if nums.count(nums[i])>1:
                index = []
                index.append(i)
                for j in range(i+1,len(nums)):
                    if nums[j]==nums[i]:
                        index.append(j)
                    if max(index)-min(index)<=k and len(index)>1:
                        return True
        return False

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        for i in xrange(len(nums)):
            if nums[i] in num_map and i - num_map[nums[i]] <= k:
                return True
            else:
                num_map[nums[i]] = i
        return False
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                if i - nums_dict[nums[i]] <= k:
                    return True
                nums_dict[nums[i]] = i
        return False
a =Solution()
print(a.containsNearbyDuplicate([1,0,1,1],1))

