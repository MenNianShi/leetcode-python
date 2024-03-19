import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int] L>=W  L*W = area  求min(L-W)
        """
        k = int(math.sqrt(area))
        for i in range(k,area+1):
            if area % i==0 and i>= area//i:
                return [i,area//i]






a = Solution()
print(a.constructRectangle(2))
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid=int(math.sqrt(area))
        while(mid>0):
            if area%mid==0:
                return[int(area/mid),int(mid)]
            mid-=1
# 492.构造矩形  .py