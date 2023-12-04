class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        g = [[] for i in range(len(roads) + 1)]
        for e in roads:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        self.res = 0

        def dfs(cur, fa):

            peopleSum = 1
            for ne in g[cur]:
                if ne != fa:
                    peopleCnt = dfs(ne, cur)
                    peopleSum += peopleCnt
                    self.res += (peopleCnt + seats - 1) // seats
            return peopleSum

        dfs(0, -1)
        return self.res
