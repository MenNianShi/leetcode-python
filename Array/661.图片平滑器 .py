# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        dx, dy = [-1, 0, 1], [-1, 0, 1]
        w, h = len(M), len(M[0])
        N = []
        for x in range(w):
            row = []
            for y in range(h):#这里的处理跟洪水填充733，有异曲同工之妙
                nbs = [M[x + i][y + j] for i in dx for j in dy \
                       if 0 <= x + i < w and 0 <= y + j < h]
                row.append(sum(nbs) / len(nbs))
            N.append(row)
        return N
# 661.图片平滑器 .py