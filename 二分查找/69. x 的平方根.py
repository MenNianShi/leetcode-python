# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
class Solution(object):
    def mySqrt(self,x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mySqrt1(self, n):
        """
        :type x: int
        :rtype: int
        """
        if n == 0: return 0
        eps = 0.0000001
        result = float(n)
        while True:
            lastvalue = result
            result = result - result / 2.0 + n / 2.0 / result
            if abs(result - lastvalue) < eps:
                break
        return int(result)

# 69. x 的平方根.py