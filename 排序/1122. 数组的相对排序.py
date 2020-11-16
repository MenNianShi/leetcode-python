# 给你两个数组，arr1 和 arr2，
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
#
#  
#
# 示例：
#
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        diff_arr2 = []
        for num in arr1:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
            if num not in arr2:
                diff_arr2.append(num)
        res = []
        diff_arr2.sort()
        for num in arr2:
            res = res + [num]* num_dict[num]
        return  res + diff_arr2
a=Solution()
print(a.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))



