class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和+哈希表
        n = len(nums)
        if n < 2: return 0

        # 前缀和：将0视为-1，1视为1，要找出一段和为0的区间
        sub = [0]
        for num in nums:
            if num == 0: num = -1
            sub.append(sub[-1] + num)

        # 哈希表，记录相同前缀和首次出现的位置
        dic = {}
        for idx, pre in enumerate(sub):
            if pre not in dic:
                dic[pre] = idx

        # 找到相同前缀和的位置
        res = 0
        for i in range(n + 1):
            res = max(res, i - dic[sub[i]])
        return res



# 525. 连续数组.py