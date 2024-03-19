class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        start = 0
        end = 1
        while end < len(nums):
            max_pos = 0
            for i in range(start,end):
                #  能跳到最远的距离
                max_pos = max(max_pos,i+nums[i])
            start = end  # 下一次起跳点范围开始的格子
            end = max_pos + 1 #  下一次起跳点范围结束的格子
            ans +=1 # 跳跃次数
        return ans