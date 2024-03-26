# 给出一个非负的数，用数组来表示这个数，比如说9999就是[9,9,9,9]当对这个数加一的时候，将这个数用数组的形式返回。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0: return digits
        digits = [1] + digits
        return digits


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]

        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            if val == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = val

        if carry: digits = [1] + digits
        return digits

# 66_plusOne.py