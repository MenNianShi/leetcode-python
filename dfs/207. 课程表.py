# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#  
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#  
import collections
#
# 对于图中的任意一个节点，它在搜索的过程中有三种状态，即：
#
# 「未搜索」：我们还没有搜索到这个节点；
#
# 「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成）；
#
# 「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求。
#
# 通过上述的三种状态，我们就可以给出使用深度优先搜索得到拓扑排序的算法流程，在每一轮的搜索搜索开始时，我们任取一个「未搜索」的节点开始进行深度优先搜索。
#
# 我们将当前搜索的节点 uu 标记为「搜索中」，遍历该节点的每一个相邻节点 vv：
#
# 如果 vv 为「未搜索」，那么我们开始搜索 vv，待搜索完成回溯到 uu；
#
# 如果 vv 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
#
# 如果 vv 为「已完成」，那么说明 vv 已经在栈中了，而 uu 还不在栈中，因此 uu 无论何时入栈都不会影响到 (u, v)(u,v) 之前的拓扑关系，以及不用进行任何操作。
#
# 当 uu 的所有相邻节点都为「已完成」时，我们将 uu 放入栈中，并将其标记为「已完成」。
#
# 在整个深度优先搜索的过程结束后，如果我们没有找到图中的环，那么栈中存储这所有的 nn 个节点，从栈顶到栈底的顺序即为一种拓扑排序。
#

class Solution(object):
    valid = True
    visited = []

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.edges = collections.defaultdict(list)
        self.visited = [0] * numCourses

        for info in prerequisites:
            self.edges[info[1]].append(info[0])
        for i in range(numCourses):
            if self.valid and not self.visited[i]:
                self.dfs(i)
        return self.valid

    def dfs(self, u):
        self.visited[u] = 1
        for v in self.edges[u]:
            if self.visited[v] == 0:
                self.dfs(v)
                if not self.valid:
                    return
            elif self.visited[v] == 1:
                self.valid = False
                return
        self.visited[u] = 2

a =Solution()
a.canFinish(2,[[0,1]])
import collections
class Solution:
    def canFinish(self, numCourses, prerequisites) :
        """
      :type numCourses: int
      :type prerequisites: List[List[int]]
      :rtype: bool
      """
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


