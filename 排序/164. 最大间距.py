#164 最大间距 桶排序
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        if len(nums) == 2: return abs(nums[0] - nums[1])
        minnum = min(nums)
        maxnum = max(nums)
        if maxnum == minnum: return 0

        lenth = len(nums) + 1  # 桶的大小
        record_max = [-1] * lenth  # 记录当前桶的最大值
        record_min = [10 ** 6] * lenth  # 记录当前桶的最大值
        hasnum = [False] * lenth  # 记录当前桶是否有数值
        for i in range(len(nums)):
            idx = int((nums[i] - minnum) * len(nums) / (maxnum - minnum))  # 桶的索引
            if not hasnum[idx]:
                record_max[idx] = nums[i]
                record_min[idx] = nums[i]
                hasnum[idx] = True
            else:
                record_max[idx] = max(record_max[idx], nums[i])
                record_min[idx] = min(record_min[idx], nums[i])

        res = 0
        tmp = record_max[0]
        for i in range(1, lenth):
            if hasnum[i]:
                res = max(res, record_min[i] - tmp)
                tmp = record_max[i]
        return res