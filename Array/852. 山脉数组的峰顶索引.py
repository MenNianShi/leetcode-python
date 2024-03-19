# 852.
# 山脉数组的峰顶索引
# 符合下列属性的数组
# arr
# 称为
# 山脉数组 ：
# arr.length >= 3
# 存在
# i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ...
# arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组
# arr ，返回任何满足
# arr[0] < arr[1] < ...
# arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 的下标
# i 。
#
#
#
# 示例
# 1：
#
# 输入：arr = [0, 1, 0]
# 输出：1
# 示例
# 2：
#
# 输入：arr = [0, 2, 1, 0]
# 输出：1
# 示例
# 3：
#
# 输入：arr = [0, 10, 5, 2]
# 输出：1
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pre = arr[0]
        pre_index = 0
        for i in range(1, len(arr)):
            if arr[i] >= pre:
                pre = arr[i]
                pre_index = i
            else:
                return pre_index

# 852. 山脉数组的峰顶索引.py