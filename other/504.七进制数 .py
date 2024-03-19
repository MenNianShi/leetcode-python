def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    s =''
    while num!=1:
        s = str(num%2)+s
        num = num//2
    s = '1'+s
    return s
print(convertToBase7(5))
def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    s =''
    if num>=0:
        while num>=7:
            s = str(num%7)+s
            num = num//7
        s = str(num)+s
        return s
    else:
        num = -num
        while num>=7:
            s = str(num%7)+s
            num = num//7
        s = '-'+str(num)+s
        return s
print(convertToBase7(-7))

# 504.七进制数 .py