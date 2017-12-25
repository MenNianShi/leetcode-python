# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            if mask & n:
                ans |= 1
            n >>= 1
        return ans
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = str(bin(n))
        pad = (32 - len(res) + 2) * "0"
        # print res
        return int(res[0:2] + res[2:][::-1] + pad, 2)