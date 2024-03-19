# 给定两个数组，编写一个函数来计算它们的交集。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#  
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        ans = []
        for n in nums2:
            if n in c1 and c1[n] > 0:
                ans.append(n)
                c1[n] -= 1
        return ans

# 350. 两个数组的交集 II.py