# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。
#
#  
#
# 示例 1：
#
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
#
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)

        return build(S) == build(T)



class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        s_stack = self.getstr([], S)
        t_stack = self.getstr([], T)
        if s_stack == t_stack:
            return True
        else:
            return False

    def getstr(self, stack, s):
        for letter in s:
            if letter != '#':
                stack.append(letter)
            else:
                if len(stack)>0:
                    stack.pop(-1)
        return stack


a = Solution()
print(a.backspaceCompare("ab##", "a#c#"))
