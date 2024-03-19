# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 示例:
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # 确定左右边界，子数组最小值为数组中最大元素，最大值为所有元素的和
        #所有子数组的和 比在left 和 right 之间
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left+ (right-left)//2
            if self.check(nums,m,mid): #  使用mid作为子数组之和上限，分割数组，如果子数组数量<=m.说明 这个mid 太大了，需要减小。
                right = mid-1
            else:
                left = mid+1
        return left
    def check(self,nums,m,mid):
        cnt = 1
        cur_sum = 0
        for num in nums:
            if cur_sum+num <= mid:
                cur_sum += num
            else:
                cur_sum = num
                cnt+=1
        return cnt<=m

# 410. 分割数组的最大值.py