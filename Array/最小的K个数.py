class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        if k == len(tinput):
            return sorted(tinput)
        l, r = 0, len(tinput) - 1
        index = self.partition(tinput, l, r)
        while index != k - 1:
            if index > k - 1:
                r = index - 1
            else:
                l = index + 1
            index = self.partition(tinput, l, r)
        return tinput[:index + 1]

    def partition(self, tinput, l, r):
        pivot = tinput[r]
        i = l - 1
        for j in range(l, r):
            if tinput[j] <= pivot:
                i += 1
                tinput[i], tinput[j] = tinput[j], tinput[i]

        tinput[i + 1], tinput[r] = tinput[r], tinput[i + 1]
        return i + 1
a = Solution()
print(a.GetLeastNumbers_Solution([4,5,2,3,1],3))
# 最小的K个数.py