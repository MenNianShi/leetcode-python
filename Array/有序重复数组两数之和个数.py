import math
def solve(arr,t):
    left,right = 0,len(arr)-1
    cnt=0
    num_dict = {}
    for num in arr:
        if num not in num_dict:
            num_dict[num]=1
        else:
            num_dict[num]+=1
    while left < right:
        if arr[left]+arr[right]==t:
            if arr[left]!=arr[right]:
                cnt += num_dict[arr[left]] * num_dict[arr[right]]
            else:
                cnt += math.factorial(num_dict[arr[left]])
            while (left+1)<len(arr) and arr[left+1]==arr[left]:
                left+=1
            while (right-1)>=0 and arr[right-1]==arr[right]:
                right-=1
            left+=1
        elif arr[left]+arr[right] > t:
            right-=1
        else:
            left += 1
    return cnt
print(solve([-3,-2,-1,-1,-1,0,1,2,2,2,3],1))
def get_two_sum_enums(numbers, target):
    mark = dict()
    n = 0
    for index, value in enumerate(numbers):
        if target - value not in mark:
            if value not in mark:
                mark[value] = 1
            else:
                mark[value] += 1
        else:
            n += mark[target - value]
    return n
print(get_two_sum_enums([-3,-2,-1,-1,-1,0,1,2,2,2,3],1))
# 有序重复数组两数之和个数.py