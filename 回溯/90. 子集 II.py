# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#  
#

class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        length = len(nums)

        def backTrack(index, path):
            path.sort()
            if path not in res:
                res.append(path)
            for i in range(index, length):
                backTrack(i + 1, path + [nums[i]]) #已排序， 不用pop

        backTrack(0, [])
        return res
a = Solution()
print(a.subsetsWithDup([4,4,4,1,4]))


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def back_track(nums, start, path):
            if path[:] not in res:
                res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                back_track(nums, i + 1, path)
                path.pop()

        back_track(nums, 0, [])

        return res
# 90. 子集 II.py