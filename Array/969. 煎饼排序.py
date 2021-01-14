class Solution(object):
    res = []

    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        self.sort_cake(arr, len(arr))
        return self.res

    def sort_cake(self, cakes, n):
        if n == 1:
            return
        max_cake = 0
        max_cake_index = 0
        for i in range(n):
            if cakes[i] > max_cake:
                max_cake_index = i
                max_cake = cakes[i]
        self.reverse(cakes, 0, max_cake_index)
        self.res.append(max_cake_index + 1)
        self.reverse(cakes, 0, n - 1)
        self.res.append(n)
        self.sort_cake(cakes, n - 1)

    def reverse(self, cakes, i, j):
        while i < j:
            cakes[i], cakes[j] = cakes[j], cakes[i]
            i += 1
            j -= 1

a = Solution()
print(a.pancakeSort([1,2,3]))