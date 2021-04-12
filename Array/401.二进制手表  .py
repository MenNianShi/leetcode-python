#二进制表
def readBinaryWatch( num):
    """
    :type num: int
    :rtype: List[str]
    """
    result = []
    for h in range(0,12):
        for m in range(0,60):
            if (bin(h)+bin(m)).count('1') == num:
                result.append('%d:%02d'% (h,m))
    return result
print(readBinaryWatch(1))
