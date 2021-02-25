# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# class Solution(object):
#     def floodFill(self, image, sr, sc, newColor):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type newColor: int
#         :rtype: List[List[int]]
#         """
#         drs = [1,0,-1,0]
#         dcs = [0,1,0,-1]
#         queue = [(sr,sc)]
#         oldColor = image[sr][sc]
#         image[sr][sc] = newColor
#         while queue:
#             r,c = queue.pop()
#             for dr,dc in zip(drs,dcs):
#                 nr,nc = r+dr,c+dc
#                 if 0 <=nr<len(image) and 0<=nc<len(image[0]):
#                     if image[nr][nc]!=newColor and image[nr][nc]==oldColor:
#                         image[nr][nc]=newColor
#                         queue.append((nr,nc))
#         return image

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        start_color = image[sr][sc]
        visit = [[0]*len(image[0]) for _ in range(len(image))]
        def dfs(sr,sc):
            if sr >=0 and sr < m and sc>=0 and sc<n and visit[sr][sc]==0:
                if image[sr][sc]!=start_color :
                    return
                else:
                    image[sr][sc] = newColor
                    visit[sr][sc] = 1
                    dfs(sr+1,sc)
                    dfs(sr-1,sc)
                    dfs(sr,sc+1)
                    dfs(sr,sc-1)
            else:
                return
        dfs(sr,sc)
        return image


class Solution(object):
    visited = []

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        start_color = image[sr][sc]
        visit = [[0] * len(image[0]) for _ in range(len(image))]

        def isValid(sr, sc):
            m = len(image)
            n = len(image[0])
            if sr >= 0 and sr < m and sc >= 0 and sc < n:
                return True
            else:
                return False

        def floodFill2(sr, sc, start_color, newColor):
            if not isValid(sr, sc):
                return
            if visit != 0:
                return
            if image[sr][sc] != start_color:
                return
            image[sr][sc] = newColor
            visit[sr][sc] = 1
            floodFill2(sr + 1, sc, start_color, newColor)
            floodFill2(sr - 1, sc, start_color, newColor)
            floodFill2(sr, sc + 1, start_color, newColor)
            floodFill2(sr, sc - 1, start_color, newColor)

        floodFill2(sr, sc, start_color, newColor)
        return image
a = Solution()
print(a.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))