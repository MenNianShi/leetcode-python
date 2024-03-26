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

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        q = deque()
        for i in range(k):# 存储当前窗口最大值的下标
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans =[nums[q[0]]] # 第一个窗口
        for i in range(k,n):# i代表窗口 右边界
            # 当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。
            #为了保持队列的性质，我们会不断地将新的元素与队尾的元素相比较，
            #如果前者大于等于后者，那么队尾的元素就可以被永久地移除，我们将其弹出队列。
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 由于队列中下标对应的元素是严格单调递减的，因此此时队首下标对应的元素就是滑动窗口中的最大值。
            # 最大值可能在滑动窗口左边界的左侧，并且随着窗口向右移动，
            # 它永远不可能出现在滑动窗口中了。因此我们还需要不断从队首弹出元素，直到队首元素在窗口中为止。
            while q[0]<= i-k : # 队首元素不在窗口中，需要弹出
                q.popleft()
            ans.append(nums[q[0]])
        return ans

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