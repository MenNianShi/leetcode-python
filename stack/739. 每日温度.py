# 给你一个数组 T，这个数组存放的是近几天的天气气温，你返回一个等长的数组，计算：对于每一天，你还要至少等多少天才能等到一个更暖和的气温；如果等不到那一天，填 0。
#For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0]
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = [] #  栈存储 温度 index
        for i in range(0,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 不停比较当前温度，与栈顶index 温度
                t = stack[-1]
                stack.pop(-1)
                answer[t] = i - t
            stack.append(i)
        return answer
# 739. 每日温度.py