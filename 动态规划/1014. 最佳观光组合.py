# 已知题目要求
# res = A[i] + A[j] + i - j （i < j） 的最大值，
#
# 而对于输入中的每一个A[j]来说， 它的值A[j]和它的下标j都是固定的，所以A[j] - j的值也是固定的。
# 因此，对于每个A[j]而言， 想要求res的最大值，也就是要求A[i] + i （i < j） 的最大值，
# 所以不妨用一个变量pre_max记录当前元素A[j]之前的A[i] + i的最大值，这样对于每个
# A[j]来说，都有最大得分 = pre_max + A[j] - j，
# 再从所有A[j]的最大得分里挑出最大值返回即可。

# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
#
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
#
# 返回一对观光景点能取得的最高分。
#
#  
#
# 示例：
#
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#求最大的  A[i]+A[j]-(j-i) 等于 求 最大的  A[i]+i + A[j]-j。 保持j 不动遍历 i
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        pre_max = A[0] + 0  # 初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)  # 判断能否刷新res
            pre_max = max(pre_max, A[j] + j)  # 判断能否刷新pre_max， 得到更大的A[i] + i

        return res


