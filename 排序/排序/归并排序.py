# 归并排序的第一步，将数组按照middle进行递归拆分
# 最后分到最细之后再将其使用对两个有序数组进行排序的方法对其进行排序。
# 两个有序数组排序的方法则非常简单
# ，同时对两个数组的第一个位置进行比大小，将小的放入一个空数组，
# 然后被放入空数组的那个位置的指针往后 移一个，
# 然后继续和另外一个数组的上一个位置进行比较，
# 以此类推。到最后任何一个数组先出栈完，就将另外i一个数组里的所有元素追加到新数组后面。
def merge(left, right):#类比两有序链表合并
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
def merge_sort(numList):
    if len(numList)<=1:
        return numList
    middle = len(numList)//2
    left = merge_sort(numList[:middle])
    right = merge_sort(numList[middle:])
    return merge(left,right)
myList = [49,38,65,97,76,13,27,49]

print(merge_sort(myList))
# 归并排序.py