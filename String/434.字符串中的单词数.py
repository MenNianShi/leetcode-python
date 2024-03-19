class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        count = 0
        for i in range(0,len(s)):
            if i-1>=0:
                if s[i]==' ' and s[i-1] !=' ':
                    count+=1
        if s[-1]!=' ':
            count+=1
        return count
a= Solution()
print(a.countSegments("Hello, my name is John"))
class Solution(object):
    def countSegments(self, s):
        import re
        s = s.strip()
        if s == "":
            return 0
        else:
            return len(re.split("\s+",s))
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # str=s.strip()
        # if not str:
        #     return 0
        # return len(str.split(' '))
        return len(s.split())
# 434.字符串中的单词数.py