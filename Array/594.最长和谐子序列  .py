# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.
import collections


def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxlength = 0
    a  = set(nums)

    for i in a:
        if nums.count(i-1)!=0 or nums.count(i+1)!=0:
            left = nums.count(i)+ nums.count(i-1)
            right = nums.count(i)+ nums.count(i+1)
            if left>=right:
                if maxlength<left:
                    maxlength=left
            else:
                if maxlength<right:
                    maxlength = right
    return maxlength
print(findLHS([1,3,2,2,5,2,3,7]))
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        return max([dict[i] + dict[i + 1] for i in dict if i + 1 in dict] or [0])
# 594.最长和谐子序列  .py