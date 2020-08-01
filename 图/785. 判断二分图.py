# 给定一个无向图graph，当这个图为二分图时返回true。
#
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
#
# graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。
#
#
# 示例 1:
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释:
# 无向图如下:
# 0----1
# |    |
# |    |
# 3----2
# 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
#
# 示例 2:
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释:
# 无向图如下:
# 0----1
# | \  |
# |  \ |
# 3----2
# 我们不能将节点分割成两个独立的子集。

# 染色

# 对于图中的任意两个节点 uu 和 vv，如果它们之间有一条边直接相连，那么 uu 和 vv 必须属于不同的集合。
#
# 如果给定的无向图连通，那么我们就可以任选一个节点开始，给它染成红色。随后我们对整个图进行遍历，将该节点直接相连的所有节点染成绿色，表示这些节点不能与起始节点属于同一个集合。我们再将这些绿色节点直接相连的所有节点染成红色，以此类推，直到无向图中的每个节点均被染色。
#
# 如果我们能够成功染色，那么红色和绿色的节点各属于一个集合，这个无向图就是一个二分图；如果我们未能成功染色，即在染色的过程中，某一时刻访问到了一个已经染色的节点，并且它的颜色与我们将要给它染上的颜色不相同，也就说明这个无向图不是一个二分图。
#
# 算法的流程如下：
#
# 我们任选一个节点开始，将其染成红色，并从该节点开始对整个无向图进行遍历；
#
# 在遍历的过程中，如果我们通过节点 uu 遍历到了节点 vv（即 uu 和 vv 在图中有一条边直接相连），那么会有两种情况：
#
# 如果 vv 未被染色，那么我们将其染成与 uu 不同的颜色，并对 vv 直接相连的节点进行遍历；
#
# 如果 vv 被染色，并且颜色与 uu 相同，那么说明给定的无向图不是二分图。我们可以直接退出遍历并返回 \text{False}False 作为答案。
#
# 当遍历结束时，说明给定的无向图是二分图，返回 \text{True}True 作为答案。
#
# 我们可以使用「深度优先搜索」或「广度优先搜索」对无向图进行遍历，下文分别给出了这两种搜索对应的代码。
#
# 注意：题目中给定的无向图不一定保证连通，因此我们需要进行多次遍历，直到每一个节点都被染色，或确定答案为 \text{False}False 为止。每次遍历开始时，我们任选一个未被染色的节点，将所有与该节点直接或间接相连的节点进行染色。
#
class Solution:


    valid = True
    UNCOLORED, RED, GREEN = 0, 1, 2
    def isBipartite(self, graph):
        n = len(graph)
        self.graph = graph
        self.color = [self.UNCOLORED] * n
        for i in range(n):
            if self.color[i] == self.UNCOLORED:
                self.dfs(i,self.RED)
                if not self.valid:
                    break

        return self.valid

    def dfs(self, node, c ):

        self.color[node] = c
        cNei = (self.GREEN if c == self.RED else self.RED)
        for neighbor in self.graph[node]:
            if self.color[neighbor] == self.UNCOLORED:
                self.dfs(neighbor, cNei)
                if not self.valid:
                    return
            elif self.color[neighbor] != cNei:
                self.valid = False
                return