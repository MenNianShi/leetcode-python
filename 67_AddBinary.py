# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        return str(bin(a+b))[2:]

a = Solution()
print(a.addBinary('11','1'))


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