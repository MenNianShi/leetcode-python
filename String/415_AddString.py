# 给定两个由数字组成的字符串，对这两个字符串相加<br/>
# 注意：<br/>
# num1和num2的长度< 5100<br/>
# num1和num2只包含数字0-9<br/>
# num1和num2不包含前导0<br/>
# 你不能使用内置的BigInteger库，也不能直接把输入转换为整数。<br/>
# 基本思想是从后向前遍历字符串，依次相加。carry表示有进位为1，无进位为0，把相加的个位数存入数组，最后倒序形成字符串

class Solution:
    def addStrings(self, num1, num2):
        ## 主要是用于大数相加，对于python来说没问题
        ## 首先将长度归一化
        m = len(num1)
        n = len(num2)
        while m > n:
            num2 = '0' + num2
            n += 1
        while n > m:
            num1 = '0' + num1
            m += 1
        carry = 0
        res = ''
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            y = int(num2[i])
            cur = x + y + carry
            res = str(cur % 10) + res
            if cur > 9:
                carry = 1
            else:
                carry = 0

        if carry == 1:
            res = '1' + res
        return res 