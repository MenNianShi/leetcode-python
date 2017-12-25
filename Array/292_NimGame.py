def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    if n>=4 and n%4==0:
        return False
    else:
        return True

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)