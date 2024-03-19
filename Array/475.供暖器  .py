
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = 0
        l = []
        if len(houses)==1:
            for i in heaters:
                x = abs(i-houses[0])
                res = min(res,x)
            return res
        for i in heaters:
            if i in houses:
                houses.remove(i)
        for i in range(0,len(houses)):
            minradius = 100000000000
            for j in range(0,len(heaters)):
                if houses[i]!=heaters[j]:
                    ranges = abs(houses[i]-heaters[j])
                    minradius = min(ranges,minradius)
            l.append(minradius)
        if l == []:
            return 0
        else:
            return max(l)
a = Solution()
print(a.findRadius([1],[1,2,3,4]))
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = 0
        res = 0
        for house in sorted(houses):
            while heaters[i + 1] - house < house - heaters[i]:
                i += 1
            res = max(res, abs(heaters[i] - house))
        return res
a = Solution()
print(a.findRadius([1],[1,2,3,4]))
# 475.供暖器  .py