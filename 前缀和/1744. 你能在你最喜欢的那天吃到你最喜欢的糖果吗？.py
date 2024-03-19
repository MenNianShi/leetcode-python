class Solution:
    def canEat(self, candiesCount, queries):
        # 前缀和
        total = [0]
        for candies in candiesCount:
            total.append(total[-1] + candies)
        total.pop(0)
        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = (favoriteDay + 1) * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]

            ans.append(not (x1 > y2 or y1 < x2))

        return ans

# 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？.py