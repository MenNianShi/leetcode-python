# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。
#
# h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        left = 0
        right = len(citations)-1
        result = 0
        while left <= right:
            mid = left + (right-left)//2
            h = len(citations)-mid
            if citations[mid]<h:
                left = mid+1
            elif citations[mid]<h:
                right = mid - 1
            else:
                return h
        return len(citations) - left
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        left = 0
        right = len(citations)-1
        result = 0
        while left <= right:
            mid = left + (right-left)//2
            h = len(citations)-mid
            if citations[mid]<h:
                left = mid+1
            else:
                result = h
                right = mid-1
        return result
citations = [0]
a = Solution()
print(a.hIndex(citations))
# 275. H指数 II.py