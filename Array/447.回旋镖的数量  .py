
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    count = 0
    for i in range(0,len(points)):
        points_dict ={}
        for j in range(0,len(points)):
            distance =(points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
            if distance not in points_dict:
                points_dict[distance] = 0
            count += points_dict[distance]*2
            points_dict[distance]+=1

    return count
print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))

class Solution(object):
    def numberOfBoomerangs(self, points):
		res = 0
		for p1 in points:
			D = dict()
			for p2 in points:
				distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
				if(distance in D):
					res += D[distance]
					D[distance] += 2
				else:
					D[distance] = 2
		return res
# 447.回旋镖的数量  .py