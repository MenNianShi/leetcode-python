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
print(twoSum([2, 7, 11, 15],9))
def twoSum(numbers,target):
    num_dict = {}
    for i ,num in enumerate(numbers):
        if (target-num) in num_dict:
            return [num_dict[target-num],i+1]
        num_dict[num] = i+1