# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        # write code here
        low = 0
        high = len(a)-1
        index = self.partition(a, low, high)
        while index!=K-1:
            if index > K-1:
                high= index-1
            else:
                low = index+1
            index = self.partition(a, low, high)
        return a[K-1]
    def partition(self,a,low,high):
        base = a[high]
        i = low-1
        for j in range(low,high):
            if a[j]>=base:
                i+=1
                a[i],a[j] = a[j],a[i]
        a[i+1],a[high] = a[high],a[i+1]
        return i+1
# 数组中第K大的数.py