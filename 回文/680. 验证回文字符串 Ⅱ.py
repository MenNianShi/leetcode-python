# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
# 输入: "aba"
# 输出: True
# 示例 2:
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。

class Solution(object):
    flag = False
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1 :return True
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                if self.flag : return False
                self.flag = True
                return self.validPalindrome(s[left+1:right+1]) or self.validPalindrome(s[left:right])
            else:
                left+=1
                right-=1
        return True
# 680. 验证回文字符串 Ⅱ.py