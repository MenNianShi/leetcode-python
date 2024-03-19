#取出 n 的最低位，加入结果 res 中。然后 n 右移，res 左移。循环此过程。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        count = 32

        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n & 1
            n >>= 1
            count -= 1

        return int(bin(res), 2)


# 190. 颠倒二进制位.py