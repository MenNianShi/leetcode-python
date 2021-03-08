def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                array[i],array[j] = array[i],array[j]
    return  array
