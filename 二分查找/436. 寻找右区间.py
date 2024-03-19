# 给定一组区间，对于每一个区间 i，检查是否存在一个区间 j，它的起始点大于或等于区间 i 的终点，这可以称为 j 在 i 的“右侧”。
#
# 对于任何区间，你需要存储的满足条件的区间 j 的最小索引，这意味着区间 j 有最小的起始点可以使其成为“右侧”区间。如果区间 j 不存在，则将区间 i 存储为 -1。最后，你需要输出一个值为存储的区间值的数组。
#
# 注意:
#
# 你可以假设区间的终点总是大于它的起始点。
# 你可以假定这些区间都不具有相同的起始点。
# 示例 1:
#
# 输入: [ [1,2] ]
# 输出: [-1]
#
# 解释:集合中只有一个区间，所以输出-1。
# 示例 2:
#
# 输入: [ [3,4], [2,3], [1,2] ]
# 输出: [-1, 0, 1]
#
# 解释:对于[3,4]，没有满足条件的“右侧”区间。
# 对于[2,3]，区间[3,4]具有最小的“右”起点;
# 对于[1,2]，区间[2,3]具有最小的“右”起点。
# 示例 3:
#
# 输入: [ [1,4], [2,3], [3,4] ]
# 输出: [-1, 2, -1]
#
# 解释:对于区间[1,4]和[3,4]，没有满足条件的“右侧”区间。
# 对于[2,3]，区间[3,4]有最小的“右”起点。
#
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        index_map = {}
        origin = intervals
        for i in range(0,len(intervals)):
            index_map[str(intervals[i])] = i
        if len(intervals)<=1:
            return [-1]
        intervals = sorted(intervals,key = lambda x:x[0])
        res = []
        for i in range(0,len(origin)):
            cur = origin[i]
            if i+1 > len(intervals):
                res.append(-1)
                continue
            else:
                index = self.binSearch(intervals,cur[1])
                if index == -1:
                    res.append(-1)
                else :
                    res.append(index_map[str(intervals[index])])
        return res

    def binSearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <=right :
            mid = left+(right-left)//2
            if nums[mid][0]==target:
                return mid
            elif nums[mid][0]>target:
                right = mid-1
            else:
                left = mid+1
        return  left if nums[-1][0]>target else -1


a = Solution()
print(a.findRightInterval([[4,5],[2,3],[1,2]]))
# 436. 寻找右区间.py