# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
#
# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            temp = num
            while temp >0:
                current = temp%10
                if current == 0 or num%current !=0:
                    return False
                temp//= 10
            return True
        return filter(is_self_dividing, range(left, right+1))
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        flag = True
        for i in range(left,right+1):
            number = str(i)
            flag = True
            for j in number:
                if int(j)==0:
                    flag = False
                else:
                    if i%int(j) != 0:
                        flag= False
            if flag == True:
                l.append(i)
        return l
a = Solution()
print(a.selfDividingNumbers(1,22))

