class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])

class Solution(object):
    def getSum(self, a, b):
        if a == 0: return b
        if b == 0: return a
        neg_bit, mask = (1 << 32) >> 1, ~(~0 << 32)
        a = (a | ~mask) if a<0 else (a & mask)
        b = (b | ~mask) if b<0  < 0 else (b & mask)
        while b:
            carry = a & b
            a = a ^ b
            a = (a | ~mask) if (a & neg_bit)  else (a & mask)
            b = carry << 1
            b = (b | ~mask) if (b & neg_bit)  else (b & mask)
        return a
# 371.两整数之和  .py