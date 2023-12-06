# 以每个点为起点进行搜索的代价会很大，因此我们考虑从 0 出发去遍历其他点（可以使用深度优先搜索或者广度优先搜索，本题解使用深度优先搜索），
# 原来我们需要统计反向边的数量，现在需要统计原方向边的数量。
#
# 具体而言，我们使用 1 标记原方向的边，使用 0 标记反向边。然后从 0 号点开始遍历，访问到某个新的点时，
# 所经过的边被 1 标记，就令答案加 1。最终统计得到的答案就是我们需要变更方向的最小路线数。


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        e = [[] for _ in range(n)]
        for edge in connections:
            e[edge[0]].append([edge[1],1])
            e[edge[1]].append([edge[0],0])
        return self.dfs(0,-1,e)
    def dfs(self, x,parent,e):
        res = 0
        for edge in e[x]:
            if edge[0] == parent:
                continue
            res += edge[1] + self.dfs(edge[0],x,e)
        return res