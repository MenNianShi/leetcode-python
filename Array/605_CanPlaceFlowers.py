# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 贪心算法（Greedy Algorithm）
#
# 从左向右遍历flowerbed，将满足要求的0设为1。计数与n比较即可。
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        for i, v in enumerate(flowerbed):
            if v: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            ans += 1
            flowerbed[i] = 1
        return ans >= n
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        placed = 0
        m = len(flowerbed)
        i = 0
        while i < m - 1:
            if flowerbed[i + 1] == 0:
                if flowerbed[i] == 0:
                    placed += 1
                i += 2
            else:
                i += 3
        if i < m and flowerbed[i] == 0:
            placed += 1
        return placed >= n
a = Solution()
print(a.canPlaceFlowers([1,0,0,0,1],1))