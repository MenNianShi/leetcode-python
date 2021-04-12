import math
def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s_sum = 0
    t_sum = 0
    for i in range(0,len(s)):
        s_sum += ord(s[i])
    for j in range(0,len(t)):
        t_sum += ord(t[j])

    return chr(t_sum-s_sum)
print(findTheDifference('abcd','abcde'))


def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    return chr(reduce(operator.xor, map(ord, (s + t))))
def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    dictionary={}
    for ch in t:
        if ch in dictionary:
            dictionary[ch]=dictionary[ch]+1
        else:
            dictionary[ch]=1
    for ch in s:
        dictionary[ch]=dictionary[ch]-1
    for i in dictionary.keys():
        if dictionary[i]!=0:
            return i