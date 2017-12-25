#判断一个数是否是回文数
#每次提取头尾两个数，判断它们是否相等，判断后去掉头尾两个数。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        digits = 1
        while x/digits >= 10:
            digits *= 10

        while digits > 1:
            right = x%10
            left = x//digits
            if left != right:
                return False
            x = (x%digits) // 10
            digits /= 100
        return True
a= Solution()
print(a.isPalindrome(12221))
#考虑生成一个反转整数，通过比较反转整数和原整数是否相等来判断回文
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        y = 0
        while tmp:
            y = y*10 + tmp%10
            tmp = tmp/10
        return y == x
