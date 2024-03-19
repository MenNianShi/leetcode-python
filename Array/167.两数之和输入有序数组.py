def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left,right = 0,len(numbers)-1
    while left<right:
        if numbers[left]+numbers[right]==target:
            return [left+1,right+1]
        elif numbers[left]+numbers[right]>target:
            right= right-1
        else:
            left = left+1


class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]

print(twoSum([2, 7, 11, 15],9))
def twoSum(numbers,target):
    num_dict = {}
    for i ,num in enumerate(numbers):
        if (target-num) in num_dict:
            return [num_dict[target-num],i+1]
        num_dict[num] = i+1
# 167.两数之和输入有序数组.py