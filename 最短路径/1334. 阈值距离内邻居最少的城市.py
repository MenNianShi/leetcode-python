
# floyd
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        ans = [float('inf'), -1]
        mp = [[float('inf')] * n for _ in range(n)]

        for fr, to, weight in edges:
            mp[fr][to], mp[to][fr] = weight, weight

        for k in range(n):
            mp[k][k] = 0
            for i in range(n):
                for j in range(n):
                    mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

        for i in range(n):
            cnt = sum(mp[i][j] <= distanceThreshold for j in range(n))
            if cnt <= ans[0]:
                ans = [cnt, i]
        return ans[1]
#Dijkstra
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        ans = [float('inf'), -1]
        mp = [[float('inf')] * n for _ in range(n)]
        dis = [[float('inf')] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        for fr, to, weight in edges:
            mp[fr][to], mp[to][fr] = weight, weight

        for k in range(n):
            mp[k][k] = 0
            for i in range(n):
                for j in range(n):
                    mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

        for i in range(n):
            dis[i][i] = 0
            for j in range(n):
                t = -1
                for k in range(n):
                    if not visited[i][k] and (t == -1 or dis[i][k] < dis[i][t]):
                        t = k
                for k in range(n):
                    dis[i][k] = min(dis[i][k], dis[i][t] + mp[t][k])
                visited[i][t] = True
        for i in range(n):
            cnt = sum(dis[i][j] <= distanceThreshold for j in range(n))
            if cnt <= ans[0]:
                ans = [cnt, i]
        return ans[1]
# 1334. 阈值距离内邻居最少的城市.py