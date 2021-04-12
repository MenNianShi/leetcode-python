# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while (val in nums):
            nums.remove(val)

def removeElement(self, nums, val):
    index = 0
    for num in nums:
        if num != val:
            nums[index] = num
            index += 1

    return index

print(removeElement([3,3,3],3))


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            front = 0
            back = len(nums) - 1
            while (front <= back):
                if nums[front] == val:
                    temp = nums[front]
                    nums[front] = nums[back]
                    nums[back] = temp
                    back -= 1
                else:
                    front += 1
        nums = nums[0:front]
        return front
