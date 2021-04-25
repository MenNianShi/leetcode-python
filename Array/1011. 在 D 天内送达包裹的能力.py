# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
#
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
#
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
#
#  
#

class Solution(object):
    def canship(self,target,weights,D):
        cur = target
        for weight in weights:
            if weight>target:
                return False
            if cur < weight:
                cur = target
                D-=1
            cur -= weight

        return D>0
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = min(weights)
        right = sum(weights)
        while left<=right:
            mid = left+(right-left)//2
            if self.canship(mid,weights,D):
                right = mid -1
            else:
                left = mid + 1
        return left