# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
#
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2:
#
# 输入: 4, [[1,0],[2,0],[3,1],[3,2]]
# 输出: [0,1,2,3] or [0,2,1,3]
# 解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
#      因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
import  collections
# 210. 课程表 II.py
class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.res = []
        # 判断有向图中是否有环
        self.valid = True
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        self.visited = [0] * numCourses
        # 存储有向图
        self.edges = collections.defaultdict(list)
        for info in prerequisites:
            self.edges[info[1]].append(info[0])
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if self.valid and self.visited[i] == 0:
                self.dfs(i)
        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return self.res[::-1] if self.valid else []

    def dfs(self, u):
        self.visited[u] = 1 # 搜索中
        for v in self.edges[u]:
            if self.visited[v] == 0: # 如果「未搜索」那么搜索相邻节点
                self.dfs(v)
                if not self.valid: # 只要发现有环，立刻停止搜索
                    return
            elif self.visited[v] == 1: # 出现环，立刻停止搜索
                self.valid = False
                return
            # else : visited[v] == 2，说明v已搜索完，不做操作
        self.visited[u] = 2 # 搜索完成
        self.res.append(u) # 将节点入栈