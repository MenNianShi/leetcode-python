def reverseString(s):
    """
    :type s: str
    :rtype: str
    """

    return s[::-1]
print(reverseString('123465'))
def firstlocation():
    s = '123456789011121314'
    l = '11'
    x = s.find(l)
    print(x)
firstlocation()
def gen():
    i = 1
    while(True):
        yield i
        i=i+1
for i in gen():
    print(i)
# 344.反转字符串.py