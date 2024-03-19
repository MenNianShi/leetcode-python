# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
#
# （这里，平面上两点之间的距离是欧几里德距离。）
#
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
#
#  
#
# 示例 1：
#
# 输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释：
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
#
#
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(points)
        n = len(points[0])
        points.sort(key=lambda point: pow(point[0] ** 2 + point[1] ** 2, 0.5))
        return points[:K]
# 我们可以使用一个优先队列（大根堆）实时维护前 KK 个最小的距离平方。
#
# 首先我们将前 KK 个点的编号（为了方便最后直接得到答案）以及对应的距离平方放入优先队列中，随后从第 K+1K+1 个点开始遍历：如果当前点的距离平方比堆顶的点的距离平方要小，就把堆顶的点弹出，再插入当前的点。当遍历完成后，所有在优先队列中的点就是前 KK 个距离最小的点。im
import  heapq
class Solution:
    def kClosest(self, points, K) :
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)

        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            if dist > q[0][0]:
                heapq.heappushpop(q, (dist, i))

        ans = [points[identity] for (_, identity) in q]
        return ans



# 973. 最接近原点的 K 个点.py