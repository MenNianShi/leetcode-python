# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
class Solution:
    def nextPermutation(self, nums):
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j = len(nums)-1
            while j >i and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        left =i+1
        right = len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: return
        partition = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                partition = i
                break
        if partition == -1:
            num.reverse()
            return
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    num[i],num[partition] = num[partition],num[i]
                    break
        num[partition+1:len(num)]=num[partition+1:len(num)][::-1]
        return
# 31. 下一个排列.py