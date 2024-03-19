
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s=='':
            return True
        if '[' not in s and '(' not in s and '{' not in s:
            return False

        for i in range(0,len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if stack ==[]:
                    return False
            if s[i]== '(' or s[i]== '[' or s[i]== '{' :
                stack.append(s[i])
            if s[i] == ')' :
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if s[i] == ']' :
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if s[i] == '}' :
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        if stack==[]:
            return True
        else:
            return False

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '[':']', '{':'}'}
        arr = []
        for char in s:
            if char in dict:
                arr.append(char)
            elif len(arr) > 0 and dict[arr[-1]] == char:
                arr.pop()
            else:
                return False
        if len(arr) == 0:
            return True
        else:
            return False
# 20.有效的括号  .py