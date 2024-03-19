# 请你帮忙设计一个程序，用来找出第 n 个丑数。
#
# 丑数是可以被 a 或 b 或 c 整除的 正整数。
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        x = [ i*a for i in range(1,n+1)]
        y = [i * b for i in range(1, n+1)]
        c = [i * c for i in range(1, n+1)]
        res = sorted(list(set(x+y+c)))
        return  res[n-1]
a = Solution()
print(a.nthUglyNumber(1000000000,2,217983653,336916467))
# 1201. 丑数 III.py