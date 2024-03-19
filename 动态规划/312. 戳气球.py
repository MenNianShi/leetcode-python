# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 示例:
#
# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


#dp[i][j]表示填满开区间(i, j)能得到的最多硬币数
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        '''
        参考了两个解题的思路。
        i是起始
        j是终点
        k是宽度，从2开始，层层迭代
        t是i+1~j-1
        '''
        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                for t in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[t] * nums[j] + dp[i][t] + dp[t][j])
        return dp[0][n - 1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums
        nums.append(1)
        def helper(lst):
            if len(lst) == 3:
                return lst[1]
            mmax = 0
            for i in range(1, len(lst)  - 1):
                tmp = lst[i-1] * lst[i] * lst[i+1]
                mmax = max(mmax, tmp + helper(lst[:i] + lst[i+1:]))
            return mmax
        return helper(nums)



# 312. 戳气球.py