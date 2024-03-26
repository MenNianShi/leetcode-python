# 399. 除法求值
import  collections
from  collections import deque, defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        neighbors = defaultdict(set)
        results = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            equ = equations[i]
            a,b = equ[0],equ[1]
            neighbors[a].add(b)
            neighbors[b].add(a)
            results[a][b] = values[i]
            results[b][a] = 1 / values[i]
        def bfs (start,end):
            if start not in neighbors:
                return -1.0
            q = deque([(start,1)])
            seen = set()
            while q:
                node,v = q.popleft()
                if node == end:
                    return v
                for x in neighbors[node]:
                    if x not in seen:
                        # v = start / node
                        # k = node / x
                        # start / x = v * k
                        q.append ((x,v * results[node][x]))
                        seen.add(x)
            return -1.0

        res = []
        for query in queries:
            res.append(bfs(query[0],query[1]))
        return res