import math
#利用二分搜索查找离当前房屋最近的电暖气
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(heaters)==1:
            x = len(houses)-heaters[0]
            y = heaters[0]-1
            return max(x,y)
        else:
            left = 0
            right = 1
            res = max(heaters[0]-1,len(houses)-heaters[-1])
            while heaters[right]<=len(houses):
                r = math.ceil((heaters[right]-heaters[left]-1)/2.0)
                res = max (res,r)
                left+=1
                right+=1
            return res
a  = Solution()
print(a.findRadius([1,2,3,4],[1,4]))
# 475. 供暖器.py