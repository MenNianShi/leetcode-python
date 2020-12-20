# 给你一个数组 T，这个数组存放的是近几天的天气气温，你返回一个等长的数组，计算：对于每一天，你还要至少等多少天才能等到一个更暖和的气温；如果等不到那一天，填 0。
#For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0]
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(T)
        res = [0] * n
        for i in range(n-1,-1,-1):
            while (stack and T[stack[-1]] <= T[i]):
                stack.pop(-1)
            res[i] =  0 if len(stack)==0 else stack[-1]-i
            stack.append(i)
        return res