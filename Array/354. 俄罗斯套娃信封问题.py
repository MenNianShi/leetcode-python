# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 说明:
#先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序。之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案
#
# 在对信封按 w 进行排序以后，我们可以找到 h 上最长递增子序列的长度。、
#
# 我们考虑输入 [[1，3]，[1，4]，[1，5]，[2，3]]，如果我们直接对 h 进行 LIS 算法，我们将会得到 [3，4，5]，显然这不是我们想要的答案，因为 w 相同的信封是不能够套娃的。
#
# 为了解决这个问题。我们可以按 w 进行升序排序，若 w 相同则按 h 降序排序。则上述输入排序后为 [[1，5]，[1，4]，[1，3]，[2，3]]，再对 h 进行 LIS 算法可以得到 [5]，长度为 1，是正确的答案。这个例子可能不明显。
#
# 我们将输入改为 [[1，5]，[1，4]，[1，2]，[2，3]]。则提取 h 为 [5，4，2，3]。我们对 h 进行 LIS 算法将得到 [2，3]，是正确的答案。

from bisect import bisect_left
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])


# 354. 俄罗斯套娃信封问题.py