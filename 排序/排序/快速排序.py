#从小到大排序
def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low
#########################################
def qsort(numList,low,high):
    if low<high:
        i,j = low,high
        #设置基准数
        base = numList[i]
        while i<j:
            #如果列表后面的数比基数大或者相等，则前移一位直到有比基准数小的数出现
            while i<j and numList[j]>=base:
                j = j-1
            #如果找到比基准数小的，就把第j个元素赋值给第i个元素，此时表中i，j两个元素相等
            numList[i] = numList[j]
            #同样的方法比较前半区
            while i<j and numList[i]<=base:
                i = i+1
            numList[j] = numList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        numList[i]=base
        qsort(numList,low,i-1)
        qsort(numList,j+1,high)
    return numList
myList = [49,38,65,97,76,13,27,49]
print("Quick Sort: ")
qsort(myList,0,len(myList)-1)
print(myList)