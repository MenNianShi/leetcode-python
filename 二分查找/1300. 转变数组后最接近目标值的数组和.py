# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
#
# 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
#
# 请注意，答案不一定是 arr 中的数字。
#
#  
#
# 示例 1：
#
# 输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
# 示例 2：
#
# 输入：arr = [2,3,5], target = 10
# 输出：5
#
#
# 输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
#
#
import bisect
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans