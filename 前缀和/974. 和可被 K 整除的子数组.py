# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#
#  
#
# 示例：
#
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
import  collections
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        #前缀和 同余关系  record 的 key 为  前缀和%K   ，value 为出现次数
        #记录 record[0]=1，这样就考虑了前缀和本身被 KK 整除的情况
        record = {0:1}
        res = 0
        total = 0
        for num in A:
            total+=num
            x = total%K
            same  = record.get(x,0)
            res += same
            record[x]= same+ 1
        return  res
# 974. 和可被 K 整除的子数组.py