class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)

#因为每个数都会经历递增的过程，最后达到一个ceiling。假设数组元素最终为X，数组最小元素min需要经过X - min次增长，
# 最大元素max需要经过X - max次增长，(X - min) - (X - max) = max - min就是max不变
#其余元素包括min增长的次数，经过这些次增长后，min元素和max元素大小相等，且它俩成为当前数组最小元素。
# 然后我们再让这俩最小元素增长到当前数组最大元素（初始数组次最大元素max2）的大小，增长的次数是max2 - min，
# 最终使得这三个元素相等。每一次增长都让数组中大小相同的元素增加一个，从1到2到3~~~n，
# 故总共增加了max - min, max2(初始数组次最大元素) - min, max3 - min，，，总和就是sum - min * n