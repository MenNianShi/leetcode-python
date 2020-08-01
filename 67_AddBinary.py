# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
# class Solution:
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         a = int(a,2)
#         b = int(b,2)
#         return str(bin(a+b))[2:]
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        i = 0
        flag = False  #表示是否进位
        res = ''
        while i < len(a) and i < len(b): #一列一列比较即可
            if flag == True:
                cur = int(a[i]) + int(b[i]) + 1
                if cur == 3:
                    res += '1'
                    flag = True
                elif cur == 2:
                    res += '0'
                    flag = True
                else:
                    res += '1'
                    flag = False
            else:
                cur = int(a[i]) + int(b[i])
                if cur == 2:
                    res += '0'
                    flag = True
                elif cur == 1:
                    res += '1'
                    flag = False
                else:
                    res += '0'
                    flag = False
            i += 1
        if i < len(a): #当 len(b)<len(a)
            if flag == False:  #无进位时，直接拼接剩余的a
                res = res + a[i:]
            else:  #有进位时，需要给剩余的a +1
                res = res + self.addBinary(a[i:][::-1], '1')[::-1]  #输入反转一次，输出反转回来

        else:  #当 两字符串长度相等，且发生进位，直接末尾+1即可
            if flag == True:
                res = res + '1'

        return res[::-1]
a =Solution()
print(a.addBinary('11','1001'))

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a

        m = len(a)
        carry = False
        c = ""
        for i in range(m):
            index = m - 1 - i
            if a[index] == "0" and b[index] == "0":
                if carry:
                    c = "1" + c
                    carry = False
                else:
                    c = "0" + c
            elif a[index] == "1" and b[index] == "0":
                if carry:
                    c = "0" + c
                else:
                    c = "1" + c
            elif a[index] == "0" and b[index] == "1":
                if carry:
                    c = "0" + c
                else:
                    c = "1" + c
            elif a[index] == "1" and b[index] == "1":
                if carry:
                    c = "1" + c
                else:
                    c = "0" + c
                    carry = True
        if carry:
            c = "1" + c
        return c
a = []
a.pop()