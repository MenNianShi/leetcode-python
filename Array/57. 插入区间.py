# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#
#区间排序后， 进行合并
class Solution(object):
    def insert(self,intervals,newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged
