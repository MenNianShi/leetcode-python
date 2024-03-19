# 给你一个zheng's数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
# 示例 3：
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
from collections import deque

class MonotonicQueue(object):
    def __init__(self):
        self.data = deque()
    def push(self,num):
        while len(self.data)>0 and num > self.data[-1]:
            self.data.pop()
        self.data.append(num)
    def max_element(self):
        return self.data[0]
    def pop(self,num):
        if len(self.data)>0 and num==self.data[0]:
            self.data.popleft()

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        windows = MonotonicQueue()
        res = []
        n = len(nums)

        for i in range(n):
            if i < k-1:
                windows.push(nums[i])
            else:
                windows.push(nums[i])
                res.append( windows.max_element())
                windows.pop(nums[i-k+1])
        return res
# 239.滑动窗口最大值.py