# 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
#
# 返回这两个区间列表的交集。
#
# （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

# 首先，对于两个区间，我们用 [a1,a2] 和 [b1,b2] 表示在 A 和 B 中的两个区间，那么什么情况下这两个区间没有交集呢：
#
#
#
# 只有这两种情况，写成代码的条件判断就是这样：
#
# if b2 < a1 or a2 < b1:
#     [a1,a2] 和 [b1,b2] 无交集
# 那么，什么情况下，两个区间存在交集呢？根据命题的否定，上面逻辑的否命题就是存在交集的条件：
#
# # 不等号取反，or 也要变成 and
# if b2 >= a1 and a2 >= b1:
#     [a1,a2] 和 [b1,b2] 存在交集
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if a2 >= b1 and b2 >= a1:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res


# 986. 区间列表的交集.py