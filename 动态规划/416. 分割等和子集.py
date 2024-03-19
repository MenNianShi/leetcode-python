# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        max_num = max(nums)
        if total % 2 == 1:
            return False
        half_sum = total // 2
        if max_num > half_sum:
            return False
        # dp[i][j] 表示从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个），
        # 是否存在一种选取方案使得被选取的正整数的和等于 j。
        # 初始时，dp中的全部元素都是 false

        dp = [[False] * (half_sum + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, half_sum + 1):
                if j > num:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][half_sum]

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums%2!=0:
            return False
        half = sum_nums/2
        cur = []
        def back(nums):
            for i in range(len(nums)):
                cur.append(nums[i])
                if sum(cur)==half:
                    return True
                else:
                    back(nums[i+1:])
                cur.pop()
            return False
        return back(nums)




# 416. 分割等和子集.py