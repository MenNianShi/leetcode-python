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
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        visited = [0] * numCourses
        adjacent = [[] for _ in range(numCourses)]
        # 0表示没有访问过，1表示访问过但是没有访问完毕，2访问完毕
        def dfs(i):
            # 访问过，还没访问完又回来了，说明有环
            if visited[i] == 1:
                return False
            # 已经完全访问完毕，说明行得通
            if visited[i] == 2:
                return True
            # 遍历前标记1
            visited[i] = 1
            for j in adjacent[i]:
                if not dfs(j):
                    return False
            # 遍历后标记2
            visited[i] = 2
            # 为2的都可以加入res了
            res.append(i)
            return True
        for cur, pre in prerequisites:
            adjacent[cur].append(pre)
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res



a = Solution()
print(a.findOrder( 4, [[1,0],[2,0],[3,1],[3,2]]))


class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        invalid = False

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if invalid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    invalid = True
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if not invalid and not visited[i]:
                dfs(i)

        if invalid:
            return list()

        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]
