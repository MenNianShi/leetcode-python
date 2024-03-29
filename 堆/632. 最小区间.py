import heapq
class Solution:
    def smallestRange(self, nums):
        heap = []
        n = len(nums)
        mi = float('inf')
        ma = float('-inf')
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, i))
            mi = min(mi, nums[i][0])
            ma = max(ma, nums[i][0])

        res = [mi, ma]
        while True:
            cur = heapq.heappop(heap)
            if cur[1] == len(nums[cur[2]]) - 1:
                break
            heapq.heappush(heap, (nums[cur[2]][cur[1] + 1], cur[1] + 1, cur[2]))
            ma = max(ma, nums[cur[2]][cur[1] + 1])
            mi = heap[0][0]
            if ma - mi < res[1] - res[0]:
                res = [mi, ma]
            elif ma - mi == res[1] - res[0] and mi < res[0]:
                res = [mi, ma]
        return res
# 632. 最小区间.py