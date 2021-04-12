
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while num>=10:
        num = (num//10)+(num%10)
    return num
print(addDigits(38))


def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """

    if num <= 9:
        return num
    elif num % 9 == 0:
        return 9
    else:
        return num % 9