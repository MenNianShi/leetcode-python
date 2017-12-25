# 给定两个由数字组成的字符串，对这两个字符串相加<br/>
# 注意：<br/>
# num1和num2的长度< 5100<br/>
# num1和num2只包含数字0-9<br/>
# num1和num2不包含前导0<br/>
# 你不能使用内置的BigInteger库，也不能直接把输入转换为整数。<br/>
# 基本思想是从后向前遍历字符串，依次相加。carry表示有进位为1，无进位为0，把相加的个位数存入数组，最后倒序形成字符串

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        idx1, idx2 = len(num1), len(num2)
        while idx1 or idx2 or carry:
            digit = carry
            if idx1:
                idx1 -= 1
                digit += int(num1[idx1])
            if idx2:
                idx2 -= 1
                digit += int(num2[idx2])
            carry = digit > 9
            result.append(str(digit % 10))
        return ''.join(result[::-1])