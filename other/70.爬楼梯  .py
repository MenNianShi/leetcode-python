# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [1, 1]
        for i in range(2, n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]
class Solution(object):
    def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre+cur
        return cur
# 70.爬楼梯  .py