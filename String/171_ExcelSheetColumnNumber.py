def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    num = 0
    exp = 1
    s=s[::-1]
    for i in range(0,len(s)):
        num = num + (ord(s[i])-ord('A')+1)*exp
        exp = exp*26
    return num
print(titleToNumber('AB'))
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i,v in (enumerate(s)):
            #print(ret,ret * 26,ord(v),ord('A'))
            #print(ret*26,ord(v)-ord('A')+1)
            #print("ret1",ret)
            ret = ret * 26 + ord(v) - ord('A')+1
            #print("ret2",ret)


        return ret