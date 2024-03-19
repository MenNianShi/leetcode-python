# 给你一个整数
# columnNumber ，返回它在
# Excel
# 表中相对应的列名称。
#
# 例如：
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
# 示例
# 1：
#
# 输入：columnNumber = 1
# 输出："A"
# 示例
# 2：
#
# 输入：columnNumber = 28
# 输出："AB"
class Solution(object):
    alpha_dict = []
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        init = ord('A')
        for i in range(26):
            self.alpha_dict.append(chr(init+i))
        res = self.helper(columnNumber)
        return res
    def helper(self,x):
        if x == 0:
            return ""
        x = x - 1
        return self.helper(x//26) + self.alpha_dict[x%26]

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        length = len(columnTitle)
        res = 0
        for num in columnTitle:
            cur = (ord(num)-ord('A')+1) * 26 ^ length
            length -=1
            res += cur
        return res 
# 168. Excel表列名称.py