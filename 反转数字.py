class Solution:
    def reverse(self , x ):
        # write code here
        res = 0
        flag = 1
        if x<0:
            flag=-1
        x = abs(x)
        while x!=0:
            res = res*10 + x%10
            x = x//10
        return flag*res
A= Solution()
print(A.reverse(123))
