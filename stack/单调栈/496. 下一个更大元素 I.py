# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
#
#  
#
# 示例 1:
#
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#     对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#     对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
# 示例 2:
#
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []

        #stack 中元素 从左到右 递减。遇到比 stack[-1]大的 应该出栈
        num_dict = {i:-1 for i in nums2}
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                small_num = stack.pop(-1)
                num_dict[small_num] = num
            stack.append(num)
        res=[]
        for num in nums1:
            res.append(num_dict[num])
        return res


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(nums2)
        # stack 中元素 从左到右 递减。遇到比 stack[-1]大的 应该出栈
        num_dict = {i: -1 for i in nums2}
        res_2 = [-1]*n
        for i in range(n-1,-1,-1):
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            res_2[i] = -1 if len(stack)==0 else stack[-1]
            num_dict[nums2[i]] = res_2[i]
            stack.append(nums2[i])

        res = []
        for num in nums1:
            res.append(num_dict[num])
        return res

a = Solution()
print(a.nextGreaterElement([4,1,2],[1,3,4,2]))