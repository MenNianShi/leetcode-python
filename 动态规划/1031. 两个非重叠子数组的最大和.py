# 给你一个整数数组
# nums
# 和两个整数
# firstLen
# 和
# secondLen，请你找出并返回两个非重叠
# 子数组
# 中元素的最大和，长度分别为
# firstLen
# 和
# secondLen 。
#
# 长度为
# firstLen
# 的子数组可以出现在长为
# secondLen
# 的子数组之前或之后，但二者必须是不重叠的。
#
# 子数组是数组的一个
# 连续
# 部分。
#
#
#
# 示例
# 1：
#
# 输入：nums = [0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9]
# 长度为
# 1，[6, 5]
# 长度为
# 2。
# 示例
# 2：
#
# 输入：nums = [3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3, 8, 1]
# 长度为
# 3，[8, 9]
# 长度为
# 2。
# 示例
# 3：
#
# 输入：nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5, 6, 0, 9]
# 长度为
# 4，[0, 3, 8]
# 长度为
# 3。
#
#
# 提示：
#
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000

class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        return max(self.help(nums, firstLen, secondLen), self.help(nums, secondLen, firstLen))

    def help(self, nums, firstLen, secondLen):
        suml = 0
        for i in range(0, firstLen):
            suml += nums[i]
        maxSumL = suml
        sumr = 0
        for i in range(firstLen, firstLen + secondLen):
            sumr += nums[i]
        res = maxSumL + sumr
        j = firstLen
        for i in range(firstLen + secondLen, len(nums)):
            suml += nums[j] - nums[j - firstLen]
            maxSumL = max(maxSumL, suml)
            sumr += nums[i] - nums[i - secondLen]
            res = max(res, maxSumL + sumr)
            j += 1
        return res


class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        first_sum_dict = {}
        second_sum_dict = {}
        for i in range(0,len(nums)-firstLen+1):
            first_sum_dict[str(i)+"#" + str(i+firstLen)] = sum(nums[i:i+firstLen])
        for i in range(0,len(nums)-secondLen+1):
            second_sum_dict[str(i)+"#" + str(i+secondLen)] = sum(nums[i:i+secondLen])
        res = 0
        for first_key, first_sum in first_sum_dict.items():
            for second_key, second_sum in second_sum_dict.items():
                first_start, first_end = map(int,first_key.split("#"))
                second_start, second_end = map(int,second_key.split("#"))
                if second_start >= first_end or first_start>=second_end :
                    res = max(res, first_sum + second_sum)
        return res




a = Solution()
print(a.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))
# 1031. 两个非重叠子数组的最大和.py