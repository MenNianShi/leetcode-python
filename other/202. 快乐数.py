# 编写一个算法来判断一个数
# n
# 是不是快乐数。
#
# 「快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为
# 1，也可能是
# 无限循环
# 但始终变不到
# 1。
# 如果这个过程
# 结果为
# 1，那么这个数就是快乐数。
# 如果
# n
# 是
# 快乐数
# 就返回
# true ；不是，则返回
# false 。
#
#
#
# 示例
# 1：
#
# 输入：n = 19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
# 202. 快乐数.py