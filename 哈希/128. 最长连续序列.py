# 用哈希表存储每个端点值对应连续区间的长度
# 若数已在哈希表中：跳过不做处理
# 若是新数加入：
# 取出其左右相邻数已有的连续区间长度 left 和 right
# 计算当前数的区间长度为：cur_length = left + right + 1
# 根据 cur_length 更新最大长度 max_length 的值
# 更新区间两端点的长度值

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                l = 0
                r = 0
                if num - 1 in num_dict:
                    l = num_dict[num-1]
                if num + 1 in num_dict:
                    r = num_dict[num+1]
                num_dict[num] = 1+ l+ r
                num_dict[num+r] = 1+r + l
                num_dict[num-l] = 1+r + l
                res = max(res,num_dict[num])
        return res
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        num_set= set(nums)
        for num in num_set:
            if num-1  not in num_set:
                cur_num = num
                cur_long = 1
                while cur_num + 1 in num_set:
                    cur_num+=1
                    cur_long +=1
                res= max(res,cur_long)
        return res
# 128. 最长连续序列.py