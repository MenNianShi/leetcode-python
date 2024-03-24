class MinStack(object):

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val :
            self.min_stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == x :
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# 155.最小栈.py