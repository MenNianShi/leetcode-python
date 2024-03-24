# 150. 逆波兰表达式求值
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stack.append(int(c))
            else:
                x = stack.pop()
                y = stack.pop()
                if c =="+":
                    stack.append(x+y)
                elif c == "-":
                    stack.append(y-x)
                elif c == "*":
                    stack.append(y*x)
                elif c == "/":
                    stack.append(int(y / float(x)))
        return stack.pop()

a = Solution()
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))