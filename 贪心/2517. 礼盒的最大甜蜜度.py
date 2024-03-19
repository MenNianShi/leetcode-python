# 礼盒的甜蜜度是 kkk 种不同的糖果中，任意两种糖果价格差的绝对值的最小值。计算礼盒的甜蜜度时，可以先将 kkk 种糖果按照价格排序，然后计算相邻的价格差的绝对值，然后取出最小值。
#
# 要求甜蜜度的最大值，可以采用二分查找的方法。先假设一个甜蜜度 mid\textit{mid}mid，然后尝试在排好序的 price\textit{price}price 中找出 kkk 种糖果，并且任意两种相邻的价格差绝对值都大于 mid\textit{mid}mid。如果可以找到这样的 kkk 种糖果，则说明可能存在更大的甜蜜度，需要修改二分查找的下边界；如果找不到这样的 kkk 种糖果，则说明最大的甜蜜度只可能更小，需要修改二分查找的上边界。
#
# 在假设一个甜蜜度 mid\textit{mid}mid 后，在排好序的 price\textit{price}price 中找 kkk 种糖果时，需要用到贪心的算法。即从小到大遍历 price\textit{price}price 的元素，如果当前糖果的价格比上一个选中的糖果的价格的差大于 mid\textit{mid}mid，则选中当前糖果，否则继续考察下一个糖果。
#
# 二分查找起始时，下边界为 000，上边界为 price\textit{price}price 的最大值与最小值之差。二分查找结束时，即可得到最大甜蜜度。



class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price = sorted(price)
        left , right = 0, price[-1]-price[0]
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(price, k ,mid):
                left = mid
            else:
                right = mid - 1
        return left
    def check (self, price, k , tastiness) :
        prev = float('-inf') 
        cnt = 0
        for p in price : 
            if p - prev >= tastiness:
                cnt +=1 
                prev = p
        return cnt >= k 

# 2517. 礼盒的最大甜蜜度.py