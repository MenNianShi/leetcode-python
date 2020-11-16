# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
#
# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
#
# 请你返回排序后的数组。
#
#  
#
# 示例 1：
#
# 输入：arr = [0,1,2,3,4,5,6,7,8]
# 输出：[0,1,2,4,8,3,5,6,7]
# 解释：[0] 是唯一一个有 0 个 1 的数。
# [1,2,4,8] 都有 1 个 1 。
# [3,5,6] 有 2 个 1 。
# [7] 有 3 个 1 。
# 按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
a = 1
print(bin(1))
print(str(bin(1024)))
a = '11'
print(a.count('1'))
arr = [1024,512,256,128,64,32,16,8,4,2,1]

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        arr.sort(key = lambda x: str(bin(x)).count('1'))
        return arr
a = Solution()
print(a.sortByBits(arr))