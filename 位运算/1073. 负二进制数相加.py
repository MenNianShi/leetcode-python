# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
#
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
#
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res_10 = self.transform_10(arr1) + self.transform_10(arr2)
        if res_10 == 0: return [0]
        return self.transform_2(res_10)
    def transform_10(self,nums):
        nums = nums[::-1]
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res += pow(-2,i)
        return res
    def transform_2(self,num):
        res = []
        while num :
            a = num % -2
            if a < 0:
                res.append(1)
                num = (num-1) // -2
                continue
            res.append(a)
            num =  num // -2
        return res[::-1]


# 1073. 负二进制数相加.py