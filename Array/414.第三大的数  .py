# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
class Solution(object):
    def thirdMax(self, list):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = None
        second_max = None
        third_max = None
        for member in list:
            if member > first_max:
                third_max = second_max
                second_max = first_max
                first_max = member
            elif member > second_max and first_max != member:
                third_max = second_max
                second_max = member
            elif member > third_max and second_max != member and first_max != member:
                third_max = member
        if third_max == None:
            return first_max
        return third_max
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        else:
            l = list(nums)
            l = sorted(nums,reverse=True)
            return l[2]

a = Solution()
print(a.thirdMax([1,2,3]))