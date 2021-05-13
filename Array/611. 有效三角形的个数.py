# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
#
# 示例 1:
#
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3


class Solution:
    def triangleNumber(self, nums):
        # 思路：能构成三角形的条件为任意两边之和大于第三边，那么就需要计算C(3,2)=3种判断
        # 但这道题可以只做一种判断，首先是先排序，固定右边最长边i，从左边找到nums[l]+nums[r]>nums[i]即可
        # 因为nums[i]最长，若有上式满足，那么也必有nums[l]+nums[i]>nums[r]和nums[r]+nums[i]>nums[l]
        # l = 0 and r = i - 1, i∈[2, len(nums) - 1]
        #固定最大边 i 如果left + right > i 那么会有right - left 个满足

        if len(nums) < 3:
            return 0

        nums = sorted(nums)
        ret = 0
        #for i in range(len(nums)-1,1,-1):
        for i in reversed(range(2, len(nums))):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ret += r - l
                    r -= 1
                else:
                    l += 1
        return ret


a = Solution()
print(a.triangleNumber([2, 2, 3, 4]))
