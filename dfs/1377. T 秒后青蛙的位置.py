class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        # 生成邻接表
        G = [[] for i in range(n+1)]
        for i , j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * (n+1)
        def dfs(i ,t):
            nxt = len(G[i])
            if i > 1:
                nxt -=1
            # 每次遍历一个节点时候，如果当前节点没有后续节点，或者剩余时间为 000， 我们不能继续搜索了。此时当前节点是target ，
            # 我们返回概率 1.0， 否则返回概率为 0.0
            if nxt == 0 or t == 0 :
                return 1.0 if i == target else 0.0
            seen[i] = 1
            # 如果有后续节点，并且剩余时间不为0，我们继续深度优先搜索，如果有子节点返回概率p > 0，说明已经找到了节点
            # target ， 又因为跳到任意一个后续子节点上的机率都相同， 我们返回概率p除以后续节点个数的商，作为最后的结果。
            for j in G[i]:
                if not seen[j]:
                    p = dfs(j, t-1)
                    if p > 0:
                        return p/nxt
            return 0.0
        return dfs(1,t)