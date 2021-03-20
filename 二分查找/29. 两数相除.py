class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        MIN_INT, MAX_INT = -2147483648, 2147483647

        dividend, divisor,= abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            cur = divisor  # 第一次是cur = divisor
            multiple = 1
            while cur + cur < dividend:
                cur += cur  # 这里是将cur x 2，即直接比较divisor x 2的次方（加快比较速度）
                multiple += multiple  # 保留divisor的倍数
            dividend -= cur  # dividend 变为 dividend-cur 进行下一轮while
            res += multiple



        if not positive:
            res = -res
        return min(max(MIN_INT, res), MAX_INT)
