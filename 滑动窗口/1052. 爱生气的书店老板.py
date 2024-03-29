# 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
#
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
#
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
#
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
#  
#
# 示例：
#
# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """

        ret = 0
        l = 0
        max_num = tmp = 0
        for i in range(len(customers)):
            # 遇到当前分钟不生气，则直接添加ret，然后把顾客重置为0
            if grumpy[i] == 0:
                ret += customers[i]
                # 顾客数重置为0
                customers[i] = 0
            else:
                # 其他情况就把tmp加上当前分钟顾客数
                tmp += customers[i]
            if i - l >= X:
                # 前面一直重置了不生气的顾客，此时默认删除左边界即可
                tmp -= customers[l]
                l += 1
            max_num = max(max_num, tmp)
        return ret + max_num


# 1052. 爱生气的书店老板.py