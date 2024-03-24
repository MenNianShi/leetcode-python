class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        names = path.split("/")
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name !='.':
                stack.append(name)
        return "/" + "/".join(stack)
# 71. 简化路径