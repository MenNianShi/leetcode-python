# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0


class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[pivot] < nums[high]: # pivot 和 high 同在右侧
                high = pivot
                # 中轴元素跟右边界元素在同一半边 。这时候最小元素在中轴元素左边
                # ，将右边界指针移动到中轴元素位置
            # Case 2):
            elif nums[pivot] > nums[high]:
                #中轴元素跟右边界届元素在 不同半边 。这时候最小元素在中轴元素 右边 ，将下届指针移动到中轴元素位置右边
                low = pivot + 1
            # Case 3):
            else:
                #https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui-1-8/
                #不确定 中轴元素 为了缩小查找范围，安全的方法是将右边界指针减一
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]


# 154. 寻找旋转排序数组中的最小值 II.py