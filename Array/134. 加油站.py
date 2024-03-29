# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明: 
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
# 示例 1:
#
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# 输出: 3
#
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#双指针，理解难点：节点回退
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 只要总油量大于等于总耗油量就肯定能跑完一圈，换句话说，
        # 油的剩余量如果大于等于0就肯定能跑完一圈，
        # 那么总耗油量如果小于0，直接返回-1
        total_remain_gas = 0
        cur_gas = 0
        index = 0
        for i in range(len(gas)):
            total_remain_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                index = (i + 1) % len(gas)
                cur_gas = 0
        if total_remain_gas < 0:
            return -1
        else:
            return index

class Solution:
    def canCompleteCircuit(self, gas, cost) :
        # 环的长度
        mod = len(gas)

        # 起始点假设为 0，当前在 0 节点。
        start, cur = 0, 0

        # 把 0 节点的油都灌进去。
        oil = gas[0]

        # 当 cur + 1 == start 时说明到了终点，所以没有考虑终点到起点（两者相邻）所用的油。
        while (cur + 1) % mod != start:

            # 如果油不够开往下一节点。
            if oil < cost[cur]:
                # 说明以 start 为起始节点不行，将 start 前一位假设为起始节点。
                start = (start - 1) % mod
                # 新的起始点里面的油全都抱走，同时要计算从新的起始点
                # 到旧的的起始点（它的下一节点）所消耗的油。
                oil += gas[start] - cost[start]

            # 如果够。
            else:
                # 把消耗的油减掉。
                oil -= cost[cur]
                # 去下一个节点。
                cur = (cur + 1) % mod
                # 把新节点的油抱走。
                oil += gas[cur]

        # 返回时记得判断一下在终点时的油能否开到起点。
        return start if oil - cost[cur] >= 0 else -1


# 134. 加油站.py