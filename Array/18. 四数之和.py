# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#使用两重循环分别枚举前两个数，然后在两重循环枚举到的数之后使用双指针枚举剩下的两个数。假设两重循环枚举到的前两个数分别位于下标 ii 和 jj，其中 i<ji<j。初始时，左右指针分别指向下标 j+1j+1 和下标 n-1n−1。每次计算四个数的和，并进行如下操作：
#
# 如果和等于 target，则将枚举到的四个数加到答案中，然后将左指针右移直到遇到不同的数，将右指针左移直到遇到不同的数；
#
# 如果和小于target，则将左指针右移一位；
#
# 如果和大于target，则将右指针左移一位。

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        if not nums or len(nums)<4 :
            return  res
        nums.sort()
        length = len(nums)
        for i in range(length-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[length-3]+nums[length-2]+nums[length-1]<target:
                continue
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left,right = j+1,length-1
                while left<right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right-=1
                        right-=1
                    elif total< target:
                        left+=1
                    else:
                        right-=1
        return  res
