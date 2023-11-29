from sortedcontainers import SortedSet
# 我们可以使用一个有序集合 sss 维护所有小于 thres 的正整数，并用 thres 表示所有大于等于 thres 的正整数。对于题目描述中的两种操作：
#
# 如果要删除最小的正整数，那么当 sss 不为空时，我们删除 s 中最小的正整数，否则删除 thres 并将 thres 的值增加 1；
#
# 如果要添加一个正整数，如果它大于等于 thres，则不进行任何操作，否则将其加入 sss 中。

class SmallestInfiniteSet(object):

    def __init__(self):
        self.thres = 1
        self.s = SortedSet()

    def popSmallest(self):
        """
        :rtype: int
        """
        s_ = self.s
        if not s_:
            ans = self.thres
            self.thres += 1
            return ans
        ans = s_[0]
        s_.pop(0)
        return ans

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        s_ = self.s
        if num < self.thres:
            s_.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)