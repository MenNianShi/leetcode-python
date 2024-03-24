class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort(key = lambda x:x[1]) # 按右边界排序
        res = 1
        last_end = points[0][1]
        for point in points:
            start = point[0]
            if start > last_end:
                res+=1
                last_end = point[1]
        return res
# 452. 用最少数量的箭引爆气球