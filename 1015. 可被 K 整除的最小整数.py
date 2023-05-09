
# 给定正整数 k ，你需要找出可以被k整除的、仅包含数字1的最小正整数n。
# 返回n的长度。如果不存在这样的n ，就返回 - 1。
#
# 示例
# 1：
#
# 输入：k = 1
# 输出：1
# 解释：最小的答案是
# n = 1，其长度为1。
# 示例
# 2：
# 输入：k = 2
# 输出：-1
# 解释：不存在可被2整除的正整数n 。
# 示例
# 3：
# 输入：k = 3
# 输出：3
# 解释：最小的答案是
# n = 111，其长度为3。

class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """

        resid = 1 % k
        resid_len = 1
        resid_set = set()
        resid_set.add(resid)
        while resid != 0:
            resid = (resid * 10 + 1) % k
            resid_len += 1
            if (resid) in resid_set:
                return -1
            resid_set.add(resid)
        return resid_len