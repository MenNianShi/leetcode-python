# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return False
        divisor_sum = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                divisor_sum += i
                divisor_sum += (num/i)
        return num == divisor_sum
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        total, div = 1, 2
        while div * div <= num:
            if num % div == 0:
                total += div
                if div * div != num:
                    total += num / div
            div += 1
        return num > 1 and total == num