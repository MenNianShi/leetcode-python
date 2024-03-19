#两个queues, 轮流把除最后一个之外的都放入另一个queue中.
import collections


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        temp = self.queue
        self.queue = collections.deque([x])
        self.queue.extend(temp)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.queue:
            return None
        else:
            return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.queue:
            return True
        else:
            return False


        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
# 225.用队列实现栈 .py