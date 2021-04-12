# 使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
#
# 右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。
#
# 注意到以下性质：
#
# 左指针左边均为非零数；
#
# 右指针左边直到左指针处均为零。
#
# 因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/move-zeroes/solution/yi-dong-ling-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in xrange(i, len(nums)):
            nums[j] = 0

