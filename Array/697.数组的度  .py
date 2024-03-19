# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
import collections
# 数组maxs记录元素的最大下标
#
# 数组mins记录元素的最小下标
#
# 数组cnts记录元素的出现个数
#
# O(n)遍历即可

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins = {}
        maxs = {}
        cnts = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            maxs[num] = max(maxs.get(num, -1), idx)
            mins[num] = min(mins.get(num, 0x7FFFFFFF), idx)
            cnts[num] += 1
        degree = max(cnts.values())
        ans = len(nums)
        for num in set(nums):
            if cnts[num] == degree:
                ans = min(ans, maxs[num] - mins[num] + 1)
        return ans
class Solution(object):#超时
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        maxNum =[]
        maxCount=0
        for i in a:
            if nums.count(i)>maxCount:
                maxNum=[]
                maxNum.append(i)
                maxCount = nums.count(i)
            else:
                if nums.count(i)==maxCount:
                    maxNum.append(i)
        shortest = 2**31-1
        for i in maxNum:
            start = nums.index(i)
            end = len(nums)-1-nums[::-1].index(i)
            if end-start+1 < shortest:
                shortest = end-start+1
        return shortest
a = Solution()
print(a.findShortestSubArray([1,2,2,3,1,4,2]))




# 697.数组的度  .py