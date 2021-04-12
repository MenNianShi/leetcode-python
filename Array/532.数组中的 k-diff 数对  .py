# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
#
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        map = {}
        res = 0
        for num in nums:
            if num not in map:
                if num+k in map:
                    res += 1
                if num-k in map:
                    res += 1
                map[num] = 1
            elif k == 0 and map[num] == 1:
                res += 1
                map[num] += 1
        return res
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        c = collections.Counter(nums)
        return sum(c[n + k] > 1 - bool(k) for n in c.keys())


import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>0:
            return len(set(nums)&{n+k for n in nums})
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
a = Solution()
print(a.findPairs([1, 3, 1, 5, 4],0))